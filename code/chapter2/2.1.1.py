# -*- coding: utf-8 -*-
import numpy
import cv2

#---------读写图像文件

img = numpy.zeros((3,3),dtype=numpy.uint8)
print 'img:',img
print 'img.shape',img.shape

img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
print 'img:',img
print 'img.shape',img.shape


'''
	1、imread()和imwrite()函数能支持各种静态图像文件的读写
	img = cv2.imread('MyPic.png') #读取png格式的图像
	cv2.imwrite('MyPic.jpg',img)  #写入JPEG格式的文件
	2、在默认情况下，即使图像文件为灰度格式，imread（）函数也会返回BGR格式的图像。
	3、当然，添加一定的参数来约束的话，还是能读出不同格式的图像。如：
	grayImg = cv2.imread('MyPic.png',cv2.IMREAD_GRAYSCALE)
	4、不论采用哪种模式，imread（）函数都会删除alpha通道的信息，得出完全不透明图像的数据。

'''























