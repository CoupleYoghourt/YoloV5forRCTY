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
    return list(warn_list)