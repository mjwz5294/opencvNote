# -*- coding: utf-8 -*-

#图像与原始字节之间的转换

# if 0:
# 	1、一个像素通常由每个通道的一个字节表示
# 	2、灰度图8位，是一个含有字节值的二维数组。
# 	3、BGR图像24位，是一个包含有字节值的三维数组
# 	4、第一维值表示像素的y坐标，第二维值代表像素的x坐标，第三维代表颜色通道
# 	（1）一个左上角由白色像素的8位灰度图像，img[0,0]的值为255
# 	（2）一个左上角由蓝色像素的24位BGR图像，img[0,0]的值为[255,0,0]
# 	5、一幅图像的每个通道为8位的话，可将其转换为字节数组格式。
# 	imgByteArr = bytearray(img)
# 	6、当然，bytearray格式也可以转换为numpy.array形式的图像
# 	grayImg = numpy.array(grayByteArr).reshape(height,width)
# 	bgrImg = numpy.array(bgrByteArr).reshape(height,width,3)

#下面介绍一个实例，将含有随机字节的bytearray转换为灰度图像和BGR图像。

import numpy
import cv2
import os

randomByteArr = bytearray(os.urandom(120000))
flatNumpyArr = numpy.array(randomByteArr)

grayImg = flatNumpyArr.reshape(300,400)
cv2.imwrite('source/RandomGray.png',grayImg)

bgrImg = flatNumpyArr.reshape(100,400,3)
cv2.imwrite('source/RandomColor.png',bgrImg)




