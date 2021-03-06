import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
def remove_bgd(img, points):
    b,g,r = cv2.split(img)       # get b,g,r
    img = cv2.merge([r,g,b])

    marked = cv2.watershed(img, points)

    marked[marked == 1] = 0
    marked[marked > 1] = 255

    kernel = np.ones((3,3),np.uint8)
    dilation = marked

    dilation = cv2.dilate(dilation.astype(np.float32), kernel, iterations = 1)

    masked_data = cv2.bitwise_and(img, img, mask=dilation.astype(np.uint8))

    b,g,r = cv2.split(masked_data)       # get b,g,r
    rgb_img = cv2.merge([r,g,b])

    cv2.imwrite("result_img.png", rgb_img)
    plt.imshow(rgb_img)
    plt.show()



if __name__ == "__main__":
    img = cv2.imread("IMG_20190106_172105.jpg", 3)

    marker = np.zeros_like(img[:,:,0]).astype(np.int32)

    # 1
    marker[1100][1500] = 64    
    # 2
    marker[1800][1500] = 128
    # 3
    marker[3000][1500] = 192

    # background

    marker[200][50] = 1
    marker[1500][1800]=1
    marker[1600][1700]=1
    marker[1700][1700]=1
  
    remove_bgd(img, marker)