# -*- coding: utf-8 -*-
import numpy as np
import cv2

#----------------捕获摄像头的帧,下面的例子，会捕获摄像头10秒的视频信息，写入avi。
cameraCapture = cv2.VideoCapture(0)
fps = 30
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
		int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter('source/outTestVid.avi',
				cv2.VideoWriter_fourcc('I','4','2','0'),
				fps,size)

success,frame = cameraCapture.read();
numFramesRemaining = 10*fps -1
while success and numFramesRemaining>0:
	videoWriter.write(frame)
	success,frame = cameraCapture.read()
	numFramesRemaining -= 1
cameraCapture.release()
