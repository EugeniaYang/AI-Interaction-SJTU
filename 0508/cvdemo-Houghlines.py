
import cv2
import numpy as np
  
img = cv2.imread("linegraph.jpg")  #读取图片文件

cv2.namedWindow("Image")   
cv2.imshow("Image", img)  #显示该图片内容

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #图片转换为灰度格式
edges = cv2.Canny(gray, 90,110) #对图片进行边缘检测

lines = cv2.HoughLinesP(edges,1,np.pi/180,200,20,10) #通过HoughLinesP检测直线

#在图片中标识出找到的直线
for line in lines:
    x1 = int(round(line[0][0]))
    y1 = int(round(line[0][1]))
    x2 = int(round(line[0][2]))
    y2 = int(round(line[0][3]))
    cv2.line(img,(x1,y1),(x2,y2),(255,255,0),10)  

cv2.imshow('HoughLinesP',img)

cv2.waitKey (0)  #等待一定时间，让显示内容可以被看到

cv2.destroyAllWindows()  #关闭所有显示框
