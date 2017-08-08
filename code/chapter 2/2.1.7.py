# -*- coding: utf-8 -*-
import numpy as np
import cv2

#------------在窗口中显示图像与摄像头帧

clicked = False
def onMouse(event,x,y,flags,param):
	global clicked
	if event == cv2.EVENT_LBUTTONUP:
		print 'mouse'
		clicked = True

cameraCap = cv2.VideoCapture(0)
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow',onMouse)

print '显示camera feed，点击窗口或按任意键结束'
success,frame = cameraCap.read()
while success and cv2.waitKey(1) == 255 and not clicked:		#这里的条件包括：读取到视频帧，没有读取到按键，没有读取到鼠标点击
	print cv2.waitKey(1)                
	cv2.imshow('MyWindow',frame)
	success,frame =  cameraCap.read()

print 'close'
cv2.destroyWindow('MyWindow')
cameraCap.release()

#这里的waitKey（1）的判断与教程不一致，教程中说没有按键时，cv2.waitKey(1)的值应该时-1，但我这里打印结果为255

#opencv的窗口函数和waitKey()函数相互依赖。opencv窗口只有在调用waitkey()函数时才会更新，waitKey()函数只有在opencv窗口成为活动窗口时，才能捕获输入信息。

#鼠标灰调函数setMouseCallback（）有5个参数，相关介绍见教程。

#然而opencv不停工任何处理窗口时间的方法。例如当点击窗口关闭按钮时，并不能关闭应用程序（上面例子的现象是，关闭后马上又打开了）。由于opencv有限的事件处理能力和GUI处理能力，许多开发人员更喜欢将opencv集成到其他应用程序框架中。










