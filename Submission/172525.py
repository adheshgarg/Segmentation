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
    img = cv2.imread("IMG_20190106_172525.jpg", 3)

    marker = np.zeros_like(img[:,:,0]).astype(np.int32)

    # 1
    marker[980][2450] = 64
    marker[450][2700] = 64
    marker[1300][2900] = 64

    # 2
    marker[790][1000] = 128
    marker[1000][750] = 128
    marker[1200][700] = 128
    marker[1000][1200] = 128
    # 3
    marker[600][2200] = 165
    marker[780][2300] = 165


    # 5
    marker[800][1600] = 192
    marker[1300][1600] = 192
    marker[600][1700] = 192
    marker[1000][1800] = 192
    marker[1300][1800] = 192

    # background

    marker[1000][500] = 1
    marker[1000][1500] = 1
    marker[1400][1000] = 1
    marker[600][1000] = 1
    marker[400][1700] = 1
    marker[1400][1700] = 1
    marker[200][3850] = 1
    marker[1000][3850] = 1
    marker[1400][3850] = 1
    marker[200][2500] = 1
    marker[200][3000] = 1
    marker[1400][3000] = 1
    marker[1000][2000] = 1
    marker[800][2300] = 1
    marker[600][2500] = 1
    marker[900][2300] =1
    marker[800][2400] = 1
    marker[400][2700] = 1
    marker[810][2350] = 1
    marker[810][2250] = 1
    marker[780][2350] = 1
    remove_bgd(img, marker)