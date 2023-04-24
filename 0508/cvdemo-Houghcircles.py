
import cv2
import numpy as np
  
img = cv2.imread("circlesgraph.jpg")  #读取图片文件

cv2.namedWindow("Image")
cv2.imshow("Image", img)  #显示该图片内容

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #图片转换为灰度格式
edges = cv2.Canny(gray, 90,110) #对图片进行边缘检测

#通过HoughCircles方法检测圆形
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 120, param2=20,
                           maxRadius=100,minRadius=30)

#在图片中标识出找到的圆
for i in circles[0, :]:
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)  # 画出外圆
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)  # 画出圆心

cv2.imshow('HoughCircle',img)

cv2.waitKey (0)  #等待一定时间，让显示内容可以被看到

cv2.destroyAllWindows()  #关闭所有显示框

