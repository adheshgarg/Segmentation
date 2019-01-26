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
    img = cv2.imread("IMG_20190106_172607.jpg", 3)

    marker = np.zeros_like(img[:,:,0]).astype(np.int32)

    # 1
    marker[400][500] = 64
    marker[800][500] = 64
    marker[680][650] = 64
    

    # 2
    marker[350][700] = 128
    marker[780][700] = 128
    marker[900][850] = 128
    marker[350][850] = 128
    # 3
    marker[600][1200] = 165
    marker[780][1250] = 165


    # 5
    marker[400][1250] = 192
    marker[300][1230] = 192
    marker[300][1450] = 192
    marker[450][1350] = 192
    marker[620][1050] = 192
    

    # background

    marker[200][50] = 1
    marker[200][2000] = 1
    marker[200][1250] = 1
    marker[200][1750] = 1
    marker[1100][1750] = 1
    marker[700][1800] = 1
    marker[500][1500] = 1
    marker[200][1400] = 1
    marker[600][2000] = 1
    marker[800][2000] = 1
    marker[300][1500]= 1
    marker[800][600]=1
    marker[1000][500]=1
    marker[900][750]=1
    marker[590][1250]=1
    marker[300][1400]=1
    marker[900][600]=1
    marker[800][500]=1
    marker[600][1100]=1
    remove_bgd(img, marker)