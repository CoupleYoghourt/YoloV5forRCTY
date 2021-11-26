from cv2 import cv2 as cv
import numpy as np
import argparse  # 导入argparse(使用命令行传参数)
import json


class OpenPose:

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='This script is used to demonstrate OpenPose human pose estimation network '
                        'from https://github.com/CMU-Perceptual-Computing-Lab/openpose project using OpenCV. '
                        'The sample and model are simplified and could be used for a single person on the frame.')
        parser.add_argument('--input', help='Path to image or video. Skip to capture frames from camera')  # 图片或者视频的地址
        #parser.add_argument('--proto', help='Path to .prototxt')
        parser.add_argument('--proto', default="pose_deploy_linevec.prototxt", help='Path to .prototxt')
        #parser.add_argument('--model', help='Path to .caffemodel')
        parser.add_argument('--model', default="pose_iter_440000.caffemodel", help='Path to .caffemodel')

        parser.add_argument('--dataset', default='COCO', help='Specify what kind of model was trained. '
                                              'It could be (COCO, MPI, HAND) depends on dataset.')
        parser.add_argument('--thr', default=0.1, type=float, help='Threshold value for pose parts heat map')
        parser.add_argument('--width', default=368, type=int, help='Resize input to specific width.')
        parser.add_argument('--height', default=368, type=int, help='Resize input to specific height.')
        parser.add_argument('--scale', default=0.003922, type=float, help='Scale for blob.')

        self.args = parser.parse_args()

        if self.args.dataset == 'COCO':
            self.BODY_PARTS = {"Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                          "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
                          "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
                          "LEye": 15, "REar": 16, "LEar": 17, "Background": 18}

            self.POSE_PAIRS = [["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
                          ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
                          ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
                          ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
                          ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"]]

        elif self.args.dataset == 'MPI':
            self.BODY_PARTS = {"Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                          "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
                          "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
                          "Background": 15}

            self.POSE_PAIRS = [["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
                          ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
                          ["LElbow", "LWrist"], ["Neck", "Chest"], ["Chest", "RHip"], ["RHip", "RKnee"],
                          ["RKnee", "RAnkle"], ["Chest", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"]]
        else:
            assert (self.args.dataset == 'HAND')  # 请指定数据集
            self.BODY_PARTS = {"Wrist": 0,
                          "ThumbMetacarpal": 1, "ThumbProximal": 2, "ThumbMiddle": 3, "ThumbDistal": 4,
                          "IndexFingerMetacarpal": 5, "IndexFingerProximal": 6, "IndexFingerMiddle": 7, "IndexFingerDistal": 8,
                          "MiddleFingerMetacarpal": 9, "MiddleFingerProximal": 10, "MiddleFingerMiddle": 11,
                          "MiddleFingerDistal": 12,
                          "RingFingerMetacarpal": 13, "RingFingerProximal": 14, "RingFingerMiddle": 15, "RingFingerDistal": 16,
                          "LittleFingerMetacarpal": 17, "LittleFingerProximal": 18, "LittleFingerMiddle": 19,
                          "LittleFingerDistal": 20,
                          }

            self.POSE_PAIRS = [["Wrist", "ThumbMetacarpal"], ["ThumbMetacarpal", "ThumbProximal"],
                          ["ThumbProximal", "ThumbMiddle"], ["ThumbMiddle", "ThumbDistal"],
                          ["Wrist", "IndexFingerMetacarpal"], ["IndexFingerMetacarpal", "IndexFingerProximal"],
                          ["IndexFingerProximal", "IndexFingerMiddle"], ["IndexFingerMiddle", "IndexFingerDistal"],
                          ["Wrist", "MiddleFingerMetacarpal"], ["MiddleFingerMetacarpal", "MiddleFingerProximal"],
                          ["MiddleFingerProximal", "MiddleFingerMiddle"], ["MiddleFingerMiddle", "MiddleFingerDistal"],
                          ["Wrist", "RingFingerMetacarpal"], ["RingFingerMetacarpal", "RingFingerProximal"],
                          ["RingFingerProximal", "RingFingerMiddle"], ["RingFingerMiddle", "RingFingerDistal"],
                          ["Wrist", "LittleFingerMetacarpal"], ["LittleFingerMetacarpal", "LittleFingerProximal"],
                          ["LittleFingerProximal", "LittleFingerMiddle"], ["LittleFingerMiddle", "LittleFingerDistal"]]

        self.inWidth = self.args.width  # 指定宽度
        self.inHeight = self.args.height  # 指定长度
        self.inScale = self.args.scale  # 指定大小

        # 读取网络，包括模型和参数文件
        self.net = cv.dnn.readNet(cv.samples.findFile(self.args.proto), cv.samples.findFile(self.args.model))

        print("OpenPose model initial done")

    def detect(self, name_list, frame):
        frameWidth = frame.shape[1]
        frameHeight = frame.shape[0]
        inp = cv.dnn.blobFromImage(frame, self.inScale, (self.inWidth, self.inHeight),
                                   (0, 0, 0), swapRB=False, crop=False)
        self.net.setInput(inp)
        out = self.net.forward()

        ##assert(len(BODY_PARTS) <= out.shape[1])

        points = []
        for i in range(len(self.BODY_PARTS)):
            # Slice heatmap of corresponging body's part.
            heatMap = out[0, i, :, :]

            # Originally, we try to find all the local maximums. To simplify a sample
            # we just find a global one. However only a single pose at the same time
            # could be detected this way.
            _, conf, _, point = cv.minMaxLoc(heatMap)
            x = (frameWidth * point[0]) / out.shape[3]
            y = (frameHeight * point[1]) / out.shape[2]

            # Add a point if it's confidence is higher than threshold.
            points.append((int(x), int(y)) if conf > self.args.thr else None)

        for pair in self.POSE_PAIRS:  # 从17条臂依次选
            partFrom = pair[0]  # 列如第一个["Head", "Neck"] 中的pair[0]=head，可以理解为向量的起点
            partTo = pair[1]  # ["Neck", "LShoulder"]  pair[1]=LShoulder ，可以理解为向量的终点
            assert (partFrom in self.BODY_PARTS)  # 向量的起点所代表的关节点在BODY_PARTS各个关节点中
            assert (partTo in self.BODY_PARTS)

            idFrom = self.BODY_PARTS[partFrom]
            idTo = self.BODY_PARTS[partTo]

            if points[idFrom] and points[idTo]:
                cv.line(frame, points[idFrom], points[idTo], (0, 255, 0),
                        3)  # 连线，line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
                cv.ellipse(frame, points[idFrom], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)  # 标出关节点
                cv.ellipse(frame, points[idTo], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)

        self.left_wrist = points[self.BODY_PARTS['LWrist']]  # 手腕
        self.right_wrist = points[self.BODY_PARTS['RWrist']]
        self.nose = points[self.BODY_PARTS['Nose']]
        self.neck = points[self.BODY_PARTS['Neck']]
        self.lelbow = points[self.BODY_PARTS['LElbow']]

        pose = {
            "pose": "行人正在投放垃圾"
        }

        # if neck and left_wrist and right_wrist and left_wrist[1] < neck[1] and right_wrist[1] < neck[1]:
        #      cv.putText(frame,'HANDS UP',(10,100),cv.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
        # if left_wrist and right_wrist and left_wrist[1] == right_wrist[1]:
        #     cv.putText(frame, 'jiaocha', (50, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0),  2)
        '''
        if(lelbow[1]<left_wrist[1]):
            with open('pose.json', 'w') as f:
                json.dump(pose, f)

        '''

