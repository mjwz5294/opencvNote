# -*- coding: utf-8 -*-
import numpy as np
import cv2

#---------使用numpy.array访问图像数组
#像素信息与字节可以相互转换了，而array可以表达字节，所以图像信息可以很方便的用数组表示。如，将图像在[0,0]处的像素转化为白色：
img = cv2.imread('source/cat.jpg')
img[0,0]=[255,255,255] 		#numpy 提供的功能，普通python数组不能这么玩
print img.item(50,20,0)
img.itemset((50,20,0),255)	#将坐标（52,20）的当前B通道的值设为255.注意，其中B-0，G-1,R-2
print img.item(50,20,0)
img[:,:,0] = 0			#操作整个G通道，将其值设为0
cv2.imwrite('source/test.png',img)
print img.shape 		#宽、高、通道数
print img.size			#像素大小
print img.dtype			#数据类型


#通过numpy还可以设定感兴趣区域（ROI），并对其进行感兴趣的操作。如将图像的某个部分拷贝到另一个部分去
myRoi = img[0:200,0:200]
img[200:400,200:400]=myRoi
cv2.imwrite('source/testRoi.png',img)
