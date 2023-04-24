import dlib
import cv2

# 人脸图像
img = #读取人脸


# 帽子图像
hat_img = #读取
r,g,b,a = cv2.split(hat_img) 
rgb_hat = cv2.merge((r,g,b))
 # 分离alpha通道
cv2.imwrite("hat_alpha.jpg",a)



# 使用Dlib的正面人脸识别器 frontal_face_detector
detector = dlib.get_frontal_face_detector()

# Dlib的5点模型
predictor = dlib.shape_predictor("5点模型")



# 使用detector检测器来检测图像中的人脸
faces = detector(img, 1)
print("找到脸数：", len(faces))

for i, d in enumerate(faces):
    #找脸

    # 使用Predictor计算面部轮廓
    shape = predictor(img, faces[i])
    points=shape.parts()
    for i in range(shape.num_parts):
        point=(points[i].x,points[i].y)
        #cv2.circle(img, point, 1, (0, 0, 255) , 4)

    # 选取左右眼眼角的点
    point1 = shape.part(0)
    point2 = shape.part(2)
  
    # 求两点中心
    eyes_center = ((point1.x+point2.x)//2,(point1.y+point2.y)//2)
  
    #cv2.circle(img,eyes_center,3,color=(0,255,0))  
    #cv2.imshow("image",img)
    #cv2.waitKey()
  
    #  根据人脸大小调整帽子大小
    factor = 1.5
    resized_hat_h = int(round(rgb_hat.shape[0]*w/rgb_hat.shape[1]*factor))
    resized_hat_w = int(round(rgb_hat.shape[1]*w/rgb_hat.shape[1]*factor))
  
    if resized_hat_h > y:
        resized_hat_h = y-1
  
    # 根据人脸大小调整帽子大小
    resized_hat = cv2.resize(rgb_hat,(resized_hat_w,resized_hat_h))

    # 用alpha通道作为mask
    mask = cv2.resize(a,(resized_hat_w,resized_hat_h))
    mask_inv =  cv2.bitwise_not(mask)

    # 帽子相对与人脸框上线的偏移量
    dh = 20
    dw = 0
    # 原图ROI
    # bg_roi = img[y+dh-resized_hat_h:y+dh, x+dw:x+dw+resized_hat_w]
    bg_roi = img[y+dh-resized_hat_h:y+dh,(eyes_center[0]-resized_hat_w//3):(eyes_center[0]+resized_hat_w//3*2)]

    # 原图ROI中提取放帽子的区域
    bg_roi = bg_roi.astype(float)
    mask_inv = cv2.merge((mask_inv,mask_inv,mask_inv))
    alpha = mask_inv.astype(float)/255

    # 相乘之前保证两者大小一致（可能会由于四舍五入原因不一致）
    alpha = cv2.resize(alpha,(bg_roi.shape[1],bg_roi.shape[0]))
    # print("alpha size: ",alpha.shape)
    # print("bg_roi size: ",bg_roi.shape)
    bg = cv2.multiply(alpha, bg_roi)
    bg = bg.astype('uint8')

    # 提取帽子区域
    hat = cv2.bitwise_and(resized_hat,resized_hat,mask = mask)

    # 相加之前保证两者大小一致（可能会由于四舍五入原因不一致）
    hat = cv2.resize(hat,(bg_roi.shape[1],bg_roi.shape[0]))
    # 两个ROI区域相加
    add_hat = cv2.add(bg,hat)
    # cv2.imshow("add_hat",add_hat) 
  
    # 把添加好帽子的区域放回原图
    img[y+dh-resized_hat_h:y+dh,(eyes_center[0]-resized_hat_w//3):(eyes_center[0]+resized_hat_w//3*2)] = add_hat
        
    

cv2.imshow("Output", img)
cv2.imwrite("withHat.jpg", img)
cv2.waitKey(0)
  

