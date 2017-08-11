# -*- coding: utf-8 -*-
import numpy as np
import cv2

#--------------------视频文件的读写
videoCap = cv2.VideoCapture('source/test.avi')
fps = videoCap.get(cv2.CAP_PROP_FPS)
size = (int(videoCap.get(cv2.CAP_PROP_FRAME_WIDTH)),
		int(videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter('source/outTest.avi',
				cv2.VideoWriter_fourcc('I','4','2','0'),
				10,size)

print 'fps-',fps
print 'size',size
success,frame = videoCap.read();
while success:
	videoWriter.write(frame)
	success,frame = videoCap.read()

# if 0:
# 	1、VideoCapture和VideoWriter类支持视频文件读写；
# 	2、用法如上，构造函数都要传入文件名；
# 	3、VideoWriter的构造函数还要传入制定的编码器，这个选项与系统有关
