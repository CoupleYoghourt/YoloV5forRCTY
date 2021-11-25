import sys
import json
sys.path.insert(0, './yolov5')

from yolov5.utils.google_utils import attempt_download
from yolov5.models.experimental import attempt_load
from yolov5.utils.general import check_img_size, non_max_suppression, scale_coords, check_imshow, xyxy2xywh
from yolov5.utils.torch_utils import select_device, time_synchronized
from deep_sort_pytorch.utils.parser import get_config
from deep_sort_pytorch.deep_sort import DeepSort
import argparse
import cv2
import torch
import torch.backends.cudnn as cudnn
import numpy as np


palette = (2 ** 11 - 1, 2 ** 15 - 1, 2 ** 20 - 1)

def xyxy_to_tlwh(bbox_xyxy):
    tlwh_bboxs = []
    for i, box in enumerate(bbox_xyxy):
        x1, y1, x2, y2 = [int(i) for i in box]
        top = x1
        left = y1
        w = int(x2 - x1)
        h = int(y2 - y1)
        tlwh_obj = [top, left, w, h]
        tlwh_bboxs.append(tlwh_obj)
    return tlwh_bboxs


def compute_color_for_labels(label):
    """
    Simple function that adds fixed color depending on the class
    """
    color = [int((p * (label ** 2 - label + 1)) % 255) for p in palette]
    return tuple(color)


def draw_boxes(img, bbox, identities=None, offset=(0, 0)):
    # global  filename,personindex
    for i, box in enumerate(bbox):
        x1, y1, x2, y2 = [int(i) for i in box]
        x1 += offset[0]
        x2 += offset[0]
        y1 += offset[1]
        y2 += offset[1]
        # box text and bar
        id = int(identities[i]) if identities is not None else 0
        color = compute_color_for_labels(id)
        label = '{}{:d}'.format("", id)
        t_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_PLAIN, 2, 2)[0]
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
        cv2.rectangle(
            img, (x1, y1), (x1 + t_size[0] + 3, y1 + t_size[1] + 4), color, -1)
        cv2.putText(img, label, (x1, y1 +
                                 t_size[1] + 4), cv2.FONT_HERSHEY_PLAIN,1, [255, 255, 255],1)
        # personindex.append([[x1,y1],[x2,y2]])

    return img

class Track:

    # 加载相关参数，并初始化模型
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--yolo_weights', type=str, default='yolov5/weights/yolov5s.pt', help='model.pt path')
        parser.add_argument('--deep_sort_weights', type=str, default='deep_sort_pytorch/deep_sort/deep/checkpoint/ckpt.t7', help='ckpt.t7 path')
        # file/folder, 0 for webcam
        #parser.add_argument('--source', type=str, default='0', help='source')
        parser.add_argument('--source', type=str, default='data/images', help='source')
        parser.add_argument('--output', type=str, default='inference/output', help='output folder')  # output folder
        parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
        parser.add_argument('--conf-thres', type=float, default=0.7, help='object confidence threshold')
        parser.add_argument('--iou-thres', type=float, default=0.5, help='IOU threshold for NMS')
        parser.add_argument('--fourcc', type=str, default='mp4v', help='output video codec (verify ffmpeg support)')
        parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
        # parser.add_argument('--show-vid', action='store_true', help='display tracking video results')
        parser.add_argument('--show-vid', default=True, help='display tracking video results')
        parser.add_argument('--save-vid', action='store_true', help='save video tracking results')
        parser.add_argument('--save-txt', action='store_true', help='save MOT compliant results to *.txt')
        # class 0 is person, 1 is bycicle, 2 is car... 79 is oven
        # parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 16 17')
        parser.add_argument('--classes', default=0, nargs='+', type=int, help='filter by class: --class 0, or --class 16 17')
        parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
        parser.add_argument('--augment', action='store_true', help='augmented inference')
        parser.add_argument('--evaluate', action='store_true', help='augmented inference')
        parser.add_argument("--config_deepsort", type=str, default="deep_sort_pytorch/configs/deep_sort.yaml")
        self.opt = parser.parse_args()
        self.opt.img_size = check_img_size(self.opt.img_size)

        out, source, yolo_weights, deep_sort_weights, show_vid, save_vid, save_txt, imgsz, evaluate = \
            self.opt.output, self.opt.source, self.opt.yolo_weights, self.opt.deep_sort_weights, self.opt.show_vid, self.opt.save_vid, \
            self.opt.save_txt, self.opt.img_size, self.opt.evaluate

        self.cfg = get_config()
        self.cfg.merge_from_file(self.opt.config_deepsort)
        attempt_download(deep_sort_weights, repo='mikel-brostrom/Yolov5_DeepSort_Pytorch')
        self.deepsort = DeepSort(self.cfg.DEEPSORT.REID_CKPT,
                            max_dist=self.cfg.DEEPSORT.MAX_DIST, min_confidence=self.cfg.DEEPSORT.MIN_CONFIDENCE,
                            nms_max_overlap=self.cfg.DEEPSORT.NMS_MAX_OVERLAP,
                            max_iou_distance=self.cfg.DEEPSORT.MAX_IOU_DISTANCE,
                            max_age=self.cfg.DEEPSORT.MAX_AGE, n_init=self.cfg.DEEPSORT.N_INIT, nn_budget=self.cfg.DEEPSORT.NN_BUDGET,
                            use_cuda=True)

        # Initialize
        self.device = select_device(self.opt.device)
        self.half = self.device.type != 'cpu'  # half precision only supported on CUDA

        cudnn.benchmark = True

        # Load model
        self.model = attempt_load(yolo_weights, map_location=self.device)  # load FP32 model
        stride = int(self.model.stride.max())  # model stride
        self.imgsz = check_img_size(imgsz, s=stride)  # check img_size

        if self.half:
            self.model.half()  # to FP16

        # Get names
        self.names = self.model.module.names if hasattr(self.model, 'module') else self.model.names  # get class names
        print("deepSort model initial done")


    # 多目标跟踪
    def detect(self, name_list, img):
        '''
        :param name_list: 文件名列表
        :param img: 待检测图片
        :return: info_show:检测输出的文字信息
        '''
        showimg = img
        with torch.no_grad():
            # Convert
            img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
            img = np.ascontiguousarray(img)
            img = torch.from_numpy(img).to(self.device)
            img = img.half() if self.half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)

            # Inference
            pred = self.model(img, augment=self.opt.augment)[0]

            # Apply NMS
            pred = non_max_suppression(
                pred, self.opt.conf_thres, self.opt.iou_thres, classes=self.opt.classes, agnostic=self.opt.agnostic_nms)

            # Process detections
            info_show = ""
            for i, det in enumerate(pred):  # detections per image
                if det is not None and len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], showimg.shape).round()

                    xywhs = xyxy2xywh(det[:, 0:4])
                    confss = det[:, 4]
                    clss = det[:, 5]

                    # pass detections to deepsort
                    outputs = self.deepsort.update(xywhs.cpu(), confss.cpu(), showimg)

                    # draw boxes for visualization
                    if len(outputs) > 0:
                        bbox_xyxy = outputs[:, :4]
                        identities = outputs[:, -1]
                        draw_boxes(showimg, bbox_xyxy, identities)
                        # to MOT format
                        #tlwh_bboxs = xyxy_to_tlwh(bbox_xyxy)
                else:
                    self.deepsort.increment_ages()

        return info_show







