# coding=utf-8
import os
import cv2
import json
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont


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
        img = cv2ImgAddChineseText(img, content, index[0], index[1],
                                   color)  # 图片 添加的文字   位置      字体                   字体大小 字体颜色 字体粗细
    return img  # cv2.putText(img, '111', index, cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)


def plot_box(img, index, color, label=None, line_thickness=3):
    # Plots one bounding box on image img

    # tl  tf为字体
    tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
    tf = max(tl - 1, 1)  # font thickness

    # c1为矩形框左上角坐标  c2为矩形框右下角坐标   貌似rectangle函数的c1 c2位置对调也能画出矩形框
    c1, c2 = index[0], index[1]
    cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)

    if label:
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        if label == 'bin':                                  # 把bin的文字显示放到框的右上角
            c1_bak = c1
            c1 = c2[0] - t_size[0], c1[1]
            c2 = c2[0]            , c1_bak[1] - t_size[1] -3
        else:
            c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # 这行能让文本矩形框填充上色
        cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA) #(c1[0], c1[1] - 2)是文字底部最左边的位置坐标

def put_mask(img, index):
    # c1为矩形框左上角坐标  c2为矩形框右下角坐标
    c1, c2 = index[0], index[1]

    # 制作掩膜
    zeros = np.zeros((img.shape), dtype=np.uint8)
    zeros_mask = cv2.rectangle(zeros, c1, c2, color=(0, 0, 220), thickness=-1)  # thickness=-1 表示矩形框内颜色填充

    alpha = 1  # alpha 为融合时第一张图片的权重
    beta = 1  # beta  为融合时第二张图片的权重
    gamma = 0  # gamma 为亮度级上的调整，数值越大，图像越亮
    # cv2.addWeighted 将原始图片与 mask 融合
    mask_img = cv2.addWeighted(img, alpha, zeros_mask, beta, gamma)
    return mask_img


if __name__ == '__main__':

    # 得到标签以及各标签对应的颜色
    names_b = ['bin', 'empty', 'full', 'covered', 'ofc', 'trash']
    colors_b = [[255, 144, 30], [144, 74, 44], [0, 0, 255], [139, 0, 0], [255, 255, 255], [128, 128, 128]]  # BGR

    names_m = ['person_index']
    colors_m = [[0, 60, 240], [0, 255, 0]]  # BGR

    names_t = ['trash_index']

    names_w = ['face_index', 'name']
    colors_w = [0, 60, 240]  # BGR

    names_z = ['pose']
    colors_z = [255, 255, 255]  # RGB

    # 读取各个文件名称时需要用到
    jsons_name = ['b', 'm', 't', 'W', 'z']

    # 得到待处理视频的路径
    video_path = 'C:/Users/96356/Desktop/test/3.mp4'

    # 设置对每一帧处理后，重新组合成视频时的参数
    fps = 30
    size = (1920, 1080)
    '''
    cv2.VideoWriter_fourcc(‘I’,’4’,’2’,’0’)，该参数是 YUV 编码类型，文件名后缀为.avi
    cv2.VideoWriter_fourcc(‘P’,’I’,’M’,’I’)，该参数是 MPEG-1 编码类型，文件名后缀为.avi
    cv2.VideoWriter_fourcc(‘X’,’V’,’I’,’D’)，该参数是 MPEG-4 编码类型，文件名后缀为.avi
    cv2.VideoWriter_fourcc(‘T’,’H’,’E’,’O’)，该参数是 Ogg Vorbis，文件名后缀为.ogv
    cv2.VideoWriter_fourcc(‘F’,’L’,’V’,1)，该参数是 Flash 视频，文件名后缀为.flv

    下面几种都是mp4的
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    '''
    # fourcc = cv2.VideoWriter_fourcc(*'XVID') 之前avi用的
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output = cv2.VideoWriter('C:/Users/96356/Desktop/3.mp4', fourcc, fps, size)

    # 进行处理
    vc = cv2.VideoCapture(video_path)
    frame_cnt = 0
    ret = True
    if vc.isOpened():
        print('视频读取成功，正在进行处理...')
        while ret:  # 循环读取视频帧
            ret, frame = vc.read()  # frame为一帧图像，当frame为空时，ret返回false，否则为true
            if frame is None:  # 图像为空，说明读完了，就可以结束循环了
                break

            # 该帧不为空时，对其进行处理
            img = frame.copy()
            for i in range(len(jsons_name)):
                file_name = 'C:/Users/96356/Desktop/info3/' + jsons_name[i] + str(frame_cnt) + '.json'
                if os.path.exists(file_name):
                    with open(file_name, 'r', encoding='UTF-8') as fp:
                        info = json.load(fp)  # json文件存在，就进行读取
                        # 接下来判断是谁的json文件
                        # zhb的
                        if jsons_name[i] == 'b':
                            cnt = len(info['label'])

                            text = info['warning']

                            for j in range(cnt):  # cnt为总共有多少个标签
                                index = info['index'][j]  # 获取坐标
                                label = info['label'][j]  # 获取标签
                                for k in range(len(names_b)):
                                    cls = names_b[k]
                                    if label.find(cls) != -1:
                                        color = colors_b[k]  # 获取标签对应的颜色
                                        break
                                plot_box(img, index, color, label, 2)
                            img = plot_warning_text(img, text)

                        # mcj的
                        elif jsons_name[i] == 'm':
                            cnt = len(info['person_index'])

                            for j in range(cnt):
                                index = info['person_index'][j]
                                color = colors_m[0]
                                plot_box(img, index, color)
                        # mcj垃圾袋的跟踪
                        elif jsons_name[i] == 't':
                            cnt = len(info['trash_index'])

                            #text = info['warning']

                            for j in range(cnt):
                                index = info['trash_index'][j]
                                #label = info['label'][j]
                                #plot_box(img, index, colors_b[5], label, 2)
                                img = put_mask(img, index)

                            # img = plot_warning_text(img, text, 1)

                        # wyz的
                        elif jsons_name[i] == 'W':
                            cnt = len(info['face_index'])

                            for j in range(cnt):
                                index = info['face_index'][j]
                                color = colors_w
                                plot_box(img, index, color)

                                name = info['name'][j]
                                if name == 'Unknown':
                                    continue
                                    #name = '郑浩彬'
                                color = [255, 255, 255]  # 由于输出中文，因此要翻转一下BGR，变成RGB
                                img = cv2ImgAddChineseText(img, name, index[0][0] + 40, index[0][1], color, textSize=35)

                        # zj的
                        else:
                            index = [950, 10]
                            text = info['pose']
                            color = colors_z
                            img = cv2ImgAddChineseText(img, text, index[0], index[1], color, textSize=30)

            output.write(img)
            frame_cnt += 1

        vc.release()
        output.release()