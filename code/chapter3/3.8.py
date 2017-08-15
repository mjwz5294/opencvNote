# -*- coding: utf-8 -*-
'''
轮廓检测
轮廓检测除了其自身是一个常见任务，还作为其他很多任务的基础存在，如计算多边形边界、形状逼近、计算感兴趣区域等任务。由于numpy中的矩形区域可以使用数组切片（slice）来定义，这些任务都是与图像数据交互时的简单操作，我们在研究物体检测和跟踪时会大量使用这些技术。
'''


# import cv2  
# import numpy as np  
  
# img = cv2.imread("source/cat.jpg")  
# emptyImage = np.zeros(img.shape, np.uint8)  
  
# emptyImage2 = img.copy()  
  
# emptyImage3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
# #emptyImage3[...]=0  
  
# cv2.imshow("EmptyImage", emptyImage)  
# cv2.imshow("Image", img)  
# cv2.imshow("EmptyImage2", emptyImage2)  
# cv2.imshow("EmptyImage3", emptyImage3)  
# cv2.imwrite("source/cat2.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 5])  
# cv2.imwrite("source/cat3.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])  
# cv2.imwrite("source/cat.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])  
# cv2.imwrite("source/cat2.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])  
# cv2.waitKey (0)  
# cv2.destroyAllWindows()




import cv2  
import numpy as np  
  
img = cv2.imread("source/cat.jpg")  
  
b = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)  
g = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)  
r = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)  
  
b[:,:] = img[:,:,0]  
g[:,:] = img[:,:,1]  
r[:,:] = img[:,:,2]  
  
merged = cv2.merge([b,g,r])  
print "Merge by OpenCV"   
print merged.strides  
print merged  
  
mergedByNp = np.dstack([b,g,r])   
print "Merge by NumPy "   
print mergedByNp.strides  
print mergedByNp  
  
cv2.imshow("Merged", merged)  
cv2.imshow("MergedByNp", merged)  
cv2.imshow("Blue", b)  
cv2.imshow("Red", r)  
cv2.imshow("Green", g)  
cv2.waitKey(0)  
cv2.destroyAllWindows()