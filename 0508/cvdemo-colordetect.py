
import cv2
import numpy as np
  
img = cv2.imread("grass.jpg")  #读取图片文件

cv2.namedWindow("Image")   
cv2.imshow("Image", img)  #显示该图片内容

img_cvtHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)   #图片转换HSV空间

lower_red = np.array([0,200,50])  #设定红色HSV值下限
upper_red = np.array([17,255,255]) #设定红色HSV值上限

mask = cv2.inRange(img_cvtHSV, lower_red, upper_red) #获取mask
cv2.imshow('Mask', mask)

res = cv2.bitwise_and(img, img, mask=mask) #图像按位操作
cv2.imshow('Result', res)

cv2.waitKey (0)  #等待一定时间，让显示内容可以被看到

cv2.destroyAllWindows()  #关闭所有显示框
