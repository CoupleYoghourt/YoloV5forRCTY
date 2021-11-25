import sys
import cv2
import time
import argparse
import torch
import numpy as np
import torch.backends.cudnn as cudnn

from utils.torch_utils import select_device
from models.experimental import attempt_load
from utils.general import check_img_size, non_max_suppression, scale_coords
from utils.datasets import letterbox
from utils.plots import plot_one_box
from utils.plots import plot_one_box2
from PIL import Image, ImageDraw, ImageFont

from selfDeepSort import Track


#from PyQt5.QtUiTools import QUiLoader
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from lib.share import shareInfo  # 公共变量名

from ui.team.team import Ui_MainWindow
#from ui.detect_ui import Ui_MainWindow

def cv2ImgAddChineseText(img, text, left, top, textColor, textSize=25):
    textColor = tuple(textColor)  # 好像外面传元祖进来的时候，到函数里面会变成list
    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    draw = ImageDraw.Draw(img)  # 创建一个可以在给定图像上绘图的对象
    fontStyle = ImageFont.truetype("simhei.ttf", textSize, encoding="utf-8")  # 字体的格式
    draw.text((left, top), text, textColor, font=fontStyle)  # 绘制文本
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)  # 转换回OpenCV格式


def plot_warning_text(img, text, flag=0):
    text.sort()  # 让每次显示的字符串的顺序都一样
    color = (0, 255, 0)  # 平常是RGB 比如RGB(255,0,0) 红色
    # opencv中的颜色通道对应是BGR 比如BGR(0,0,255) 红色
    ori_index = [10, 10]
    if '正常' not in text:
        color = [255, 215, 0]  # 其他提示的文字的颜色，由于底下用的是PIL库的写字工具，因此颜色通道仍是RGB
        color_e = (255, 215, 0)  # "异常"两字的颜色，RGB
        img = cv2ImgAddChineseText(img, "异常：", ori_index[0], ori_index[1], color_e)
        ori_index[1] += 30

    for i in range(len(text)):
        content = text[i]
        index = (ori_index[0], ori_index[1] + i * 30)
        img = cv2ImgAddChineseText(img, content, index[0], index[1], color)  # 图片 添加的文字   位置      字体                   字体大小 字体颜色 字体粗细

    return img  # cv2.putText(img, '111', index, cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)


class win_Main(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        #self.ui = QUiLoader().load('ui/team/team.ui')
        super(win_Main, self).__init__(parent)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.timer_video = QtCore.QTimer()  # 创建定时器
        self.init_slots()
        # self.cap = cv2.VideoCapture()
        self.num_stop = 1  # 暂停与播放辅助信号，note：通过奇偶来控制暂停与播放
        self.output_folder = 'output/'
        self.vid_writer = None

    # 控件绑定相关操作
    def init_slots(self):
        self.ui.pushButton_img.clicked.connect(self.button_image_open)
        self.ui.pushButton_video.clicked.connect(self.button_video_open)
        self.ui.pushButton_camer.clicked.connect(self.button_camera_open)
        self.ui.pushButton_stop.clicked.connect(self.button_video_stop)
        self.ui.pushButton_start.clicked.connect(self.button_video_stop)


        self.ui.pushButton_finish.clicked.connect(self.finish_detect)

        self.timer_video.timeout.connect(self.show_video_frame)  # 定时器超时，将槽绑定至show_video_frame

        self.model_init()
        self.trackPerson = Track()

    # 加载相关参数，并初始化模型
    def model_init(self):
        # 模型相关参数配置
        parser = argparse.ArgumentParser()
        parser.add_argument('--weights', nargs='+', type=str, default='weights/best.pt', help='model.pt path(s)')
        parser.add_argument('--source', type=str, default='0', help='source')  # file/folder, 0 for webcam
        parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
        parser.add_argument('--conf-thres', type=float, default=0.5, help='object confidence threshold')
        parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
        parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
        parser.add_argument('--view-img', action='store_true', help='display results')
        parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
        parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
        parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
        parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
        parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
        parser.add_argument('--augment', action='store_true', help='augmented inference')
        parser.add_argument('--update', action='store_true', help='update all models')
        parser.add_argument('--project', default='runs/detect', help='save results to project/name')
        parser.add_argument('--name', default='exp', help='save results to project/name')
        parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
        self.opt = parser.parse_args()
        print(self.opt)
        # 默认使用opt中的设置（权重等）来对模型进行初始化
        source, weights, view_img, save_txt, imgsz = self.opt.source, self.opt.weights, self.opt.view_img, self.opt.save_txt, self.opt.img_size

        self.device = select_device(self.opt.device)
        self.half = self.device.type != 'cpu'  # half precision only supported on CUDA

        cudnn.benchmark = True

        # Load model
        self.model = attempt_load(weights, map_location=self.device)  # load FP32 model
        stride = int(self.model.stride.max())  # model stride
        self.imgsz = check_img_size(imgsz, s=stride)  # check img_size
        if self.half:
            self.model.half()  # to FP16

        # Get names and colors
        self.names = self.model.module.names if hasattr(self.model, 'module') else self.model.names
        self.colors = [[255, 144, 30], [144, 74, 44], [0, 0, 255], [139, 0, 0], [255, 255, 255], [128, 128, 128]]
        print("yolov5 model initial done")
        # 设置提示框
        # QtWidgets.QMessageBox.information(self.ui, u"Notice", u"模型加载完成", buttons=QtWidgets.QMessageBox.Ok,
        #                                  defaultButton=QtWidgets.QMessageBox.Ok)

    # 目标检测
    def detect(self, name_list, img):
        '''
        :param name_list: 文件名列表
        :param img: 待检测图片
        :return: info_show:检测输出的文字信息
        '''
        showimg = img

        # '''
        with torch.no_grad():
            img = letterbox(img, new_shape=self.opt.img_size)[0]
            # Convert
            img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
            img = np.ascontiguousarray(img)
            img = torch.from_numpy(img).to(self.device)
            img = img.half() if self.half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)
            # Inference

            print('333333333333333333333')

            pred = self.model(img, augment=self.opt.augment)[0]

            print('4444444444444444444444')
            # Apply NMS
            pred = non_max_suppression(pred, self.opt.conf_thres, self.opt.iou_thres, classes=self.opt.classes,
                                       agnostic=self.opt.agnostic_nms)
            info_show = ""
            # Process detections

            warn_list = set()
            for i, det in enumerate(pred):
                if det is not None and len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], showimg.shape).round()

                    for *xyxy, conf, cls in reversed(det):
                        if self.names[int(cls)] == 'empty':
                            warn_list.add('有垃圾桶盖子未盖')
                        elif self.names[int(cls)] == 'full':
                            warn_list.add('有垃圾桶已满')
                        elif self.names[int(cls)] == 'ofc':
                            warn_list.add('有垃圾桶已满')
                        elif self.names[int(cls)] == 'trash':
                            warn_list.add('垃圾桶附近存在垃圾')

                        label = '%s %.2f' % (self.names[int(cls)], conf)
                        name_list.append(self.names[int(cls)])
                        plot_one_box(xyxy, showimg, label=label, color=self.colors[int(cls)],
                                     line_thickness=2)

            if not warn_list:  # 说明没有异常状态
                warn_list.add('正常')

        # '''
        ###
        # self.trackPerson.detect(name_list, showimg)

        showimg = plot_warning_text(showimg, list(warn_list))
        #cv2.imshow('img234', showimg)

        info_show = ""
        for i, single_info in enumerate(warn_list):
            info_show = info_show + single_info + "\n"
        return showimg, info_show


    # 打开图片并检测
    def button_image_open(self):
        print('button_image_open')
        name_list = []
        try:
            img_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "打开图片", "data/images",
                                                                "*.jpg;;*.png;;All Files(*)")
        except OSError as reason:
            print('文件打开出错啦！核对路径是否正确' + str(reason))
        else:
            # 判断图片是否为空
            if not img_name:
                QtWidgets.QMessageBox.warning(self, u"Warning", u"打开图片失败", buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                img = cv2.imread(img_name)
                print("img_name:", img_name)
                showimg, info_show = self.detect(name_list, img)
                print(info_show)
                # 获取当前系统时间，作为img文件名
                now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
                file_extension = img_name.split('.')[-1]
                new_filename = now + '.' + file_extension  # 获得文件后缀名
                file_path = self.output_folder + 'img_output/' + new_filename
                cv2.imwrite(file_path, img)
                # 检测信息显示在界面
                self.ui.textBrowser.setText(info_show)

                # 检测结果显示在界面
                self.result = cv2.cvtColor(showimg, cv2.COLOR_BGR2BGRA)
                self.result = cv2.resize(self.result, (640, 480), interpolation=cv2.INTER_AREA)
                self.QtImg = QtGui.QImage(self.result.data, self.result.shape[1], self.result.shape[0],
                                          QtGui.QImage.Format_RGB32)
                self.ui.label.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
                self.ui.label.setScaledContents(True)  # 设置图像自适应界面大小


    def set_video_name_and_path(self):
        # 获取当前系统时间，作为img和video的文件名
        now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        # if vid_cap:  # video
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        w = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # 视频检测结果存储位置

        save_path = self.output_folder + 'video_output/' + now + '.mp4'

        print(save_path)

        return fps, w, h, save_path

    # 打开视频并检测
    def button_video_open(self):
        video_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "打开视频", "data/", "*.mp4;;*.avi;;All Files(*)")
        self.cap = cv2.VideoCapture(video_name)
        # flag = self.cap.open(video_name)
        flag = self.cap.isOpened()
        if not flag:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"打开视频失败", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            # -------------------------写入视频----------------------------------#
            fps, w, h, save_path = self.set_video_name_and_path()
            self.vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
            self.timer_video.start(15)  # 以30ms为间隔，启动或重启定时器
            # 进行视频识别时，关闭其他按键点击功能
            self.ui.pushButton_video.setDisabled(True)
            self.ui.pushButton_img.setDisabled(True)
            self.ui.pushButton_camer.setDisabled(True)

    # 打开摄像头检测
    def button_camera_open(self):
        print("Open camera to detect")
        # 设置使用的摄像头序号，系统自带为0
        camera_num = 0
        # 打开摄像头
        self.cap = cv2.VideoCapture(camera_num)
        # 判断摄像头是否处于打开状态
        bool_open = self.cap.isOpened()
        if not bool_open:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"打开摄像头失败", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            fps, w, h, save_path = self.set_video_name_and_path()
            fps = 5  # 控制摄像头检测下的fps，Note：保存的视频，播放速度有点快，我只是粗暴的调整了FPS
            self.vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
            self.timer_video.start(15)
            self.ui.pushButton_video.setDisabled(True)
            self.ui.pushButton_img.setDisabled(True)
            self.ui.pushButton_camer.setDisabled(True)

    # 定义视频帧显示操作
    def show_video_frame(self):
        name_list = []
        flag, img = self.cap.read()
        if img is not None:
            showimg, info_show = self.detect(name_list, img)  # 检测结果写入到原始img上

            self.vid_writer.write(img)  # 检测结果写入视频
            print(info_show)
            # 检测信息显示在界面
            self.ui.textBrowser.setText(info_show)

            show = cv2.resize(showimg, (640, 480))  # 直接将原始img上的检测结果进行显示
            self.result = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
            showImage = QtGui.QImage(self.result.data, self.result.shape[1], self.result.shape[0],
                                     QtGui.QImage.Format_RGB888)
            self.ui.label.setPixmap(QtGui.QPixmap.fromImage(showImage))
            self.ui.label.setScaledContents(True)  # 设置图像自适应界面大小

        else:
            self.timer_video.stop()
            # 读写结束，释放资源
            self.cap.release()  # 释放video_capture资源
            self.vid_writer.release()  # 释放video_writer资源
            self.ui.label.clear()
            self.ui.textBrowser.clear()
            # 视频帧显示期间，禁用其他检测按键功能
            self.ui.pushButton_video.setDisabled(False)
            self.ui.pushButton_img.setDisabled(False)
            self.ui.pushButton_camer.setDisabled(False)

    # 暂停与继续检测
    def button_video_stop(self):
        self.timer_video.blockSignals(False)
        # 暂停检测
        # 若QTimer已经触发，且激活
        if self.timer_video.isActive() == True and self.num_stop % 2 == 1:
            # self.ui.pushButton_stop.setText(u'继续检测')  # 当前状态为暂停状态
            self.num_stop = self.num_stop + 1  # 调整标记信号为偶数
            self.timer_video.blockSignals(True)
        # 继续检测
        else:
            self.num_stop = self.num_stop + 1
            # self.ui.pushButton_stop.setText(u'暂停检测')

    # 结束视频检测
    def finish_detect(self):
        # self.timer_video.stop()
        self.cap.release()  # 释放video_capture资源
        self.vid_writer.release()  # 释放video_writer资源
        self.ui.label.clear()  # 清空label画布
        # 启动其他检测按键功能
        self.ui.pushButton_video.setDisabled(False)
        self.ui.pushButton_img.setDisabled(False)
        self.ui.pushButton_camer.setDisabled(False)

        # 结束检测时，查看暂停功能是否复位，将暂停功能恢复至初始状态
        # Note:点击暂停之后，num_stop为偶数状态
        if self.num_stop % 2 == 0:
            print("Reset stop/begin!")
            # self.ui.pushButton_stop.setText(u'暂停/继续')
            self.num_stop = self.num_stop + 1
            self.timer_video.blockSignals(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    current_ui = win_Main()
    current_ui.show()
    sys.exit(app.exec_())