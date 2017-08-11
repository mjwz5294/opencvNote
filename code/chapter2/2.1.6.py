# -*- coding: utf-8 -*-
import numpy as np
import cv2

#------------在窗口中显示图像与摄像头帧
img = cv2.imread('source/cat.jpg')
cv2.imshow('cat',img)
cv2.waitKey()
cv2.destroyAllWindows()	#释放由opencv创建的所有窗口

#opencv的namedWindow（）、imshow（）和DestroyWindow()函数允许指定窗口名来创建、显示和销毁窗口。此外，任意窗口下都可以通过waitKey（）函数来获取键盘输入，通过setMouseCallback（）函数来获取鼠标输入。
