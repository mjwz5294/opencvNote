# -*- coding: utf-8 -*-
import numpy
import cv2
import utils

#----------同CaptureManager和WindowsManager类一样，滤波器filter也需要能在cameo外复用。filter.py中就添加一些滤波函数和类。上面util.py，就存放一些更通用的数学函数。

'''
在下面的代码中，实现了：
使用medianBlur()作为模糊函数降噪，使用Laplacian()作为边缘检测函数生成边缘线条。在Laplacian()函数得到结果后，需要将其转换成黑色边缘和白色背景的图像。然后将其归一化（使得像素值在0到1之间），并乘以源图像，以便能将边缘变黑。

根据作者的设备，设置默认值为blurKsize = 7,edgeKsize = 5，我们可以根据自己的设备更改。blurKsize一般比edgeKsize的值更大，当其大于7时，medianBlur函数的代价会比较高。而当其比较小时，模糊效果就不明显了，小于3的时候就直接没必要用模糊效果了。
'''
def strokeEdges(src,dst,blurKsize = 7,edgeKsize = 5):
	if blurKsize>=3:
		blurredSrc = cv2.medianBlur(src,blurKsize)
		graySrc = cv2.cvtColor(blurredSrc,cv2.COLOR_BGR2GRAY)
	else:
		graySrc = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

	cv2.Laplacian(graySrc,cv2.CV_8U,graySrc,ksize = edgeKsize)
	normalizedInverseAlpha = (1.0/255)*(255-graySrc)
	channels = cv2.split(src)
	for channel in channels:
		channel[:] = channel*normalizedInverseAlpha
	cv2.merge(channels,dst)


#卷积滤波器

class VConvolutionFilter(object):
	"""docstring for VConvolutionFilter"""
	def __init__(self, kernel):
		super(VConvolutionFilter, self).__init__()
		self._kernel = kernel
	def apply(self,src,dst):
		cv2.filter2D(src,-1,self._kernel,dst)
#锐化滤波器
class SharpenFilter(VConvolutionFilter):
	"""docstring for SharpenFilter"""
	def __init__(self):
		super(SharpenFilter, self).__init__()
		kernel = numpy.array([
				[-1,-1,-1],
				[-1,9,-1],
				[-1,-1,-1]
			])
		VConvolutionFilter.__init__(self.kernel)
		
#一般权重加起来为1（如果不想改变图像亮度），下面修改一下锐化核，使其权重加起来为0，则会得到一个边缘检测核，把边缘转为白色，非边缘转为黑色
class FindEdgesFilter(VConvolutionFilter):
	"""docstring for FindEdgesFilter"""
	def __init__(self):
		super(FindEdgesFilter, self).__init__()
		self.kernel = numpy.array([
				[-1,-1,-1],
				[-1,8,-1],
				[-1,-1,-1]
			])
		VConvolutionFilter.__init__(self.kernel)
		
#下面构建一个模糊滤波器，为达到模糊效果，通常权重和应该为1，且临近像素的权重全为正（小于1，减小与周围的差值，实现模糊效果）。下面实现一个简单的临近平均滤波器：
class BlurFilter(VConvolutionFilter):
	"""docstring for BlurFilter"""
	def __init__(self):
		super(BlurFilter, self).__init__()
		kernel = ([
				[0.04,0.04,0.04,0.04,0.04],
				[0.04,0.04,0.04,0.04,0.04],
				[0.04,0.04,0.04,0.04,0.04],
				[0.04,0.04,0.04,0.04,0.04],
				[0.04,0.04,0.04,0.04,0.04],
				[0.04,0.04,0.04,0.04,0.04]
			])
		VConvolutionFilter.__init__(self.kernel)
		
#锐化、边缘检测以及模糊等滤波器都使用了高度对称的核，但有时不对称的核也能起到一些有趣的效果。下面介绍一种同时具有模糊（正权重）和锐化（负权重）的作用，这回产生一种脊状或浮雕的效果
class EmbossFilter(VConvolutionFilter):
	"""docstring for EmbossFilter"""
	def __init__(self, arg):
		super(EmbossFilter, self).__init__()
		self.kernel = numpy.array([
				[-2,-1,0],
				[-1,1,1],
				[0,1,2]
			])
		VConvolutionFilter.__init__(self.kernel)
		
















