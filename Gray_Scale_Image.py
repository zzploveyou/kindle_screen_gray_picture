#!/usr/bin/env python
# coding:utf-8
'''
Author       :  ZZP
Mail         :  zhangzhaopeng@mail.nankai.edu.cn
Created Time :  2016-04-25 12:39:28

Description  :
    get Gray Scale Image using python-cv2
    python this.py 123.png
'''
import cv2
import sys
import glob
import os


def gepic(pic_name):
    img = cv2.imread(pic_name)
    x = img.shape[0]
    y = img.shape[1]
    for i in range(x):
        for j in range(y):
            (r, g, b) = img[i, j]
            gray = r * 0.3 + g * 0.59 + b * 0.11
            # gray=(r*76+g*151+b*28)>>8
            # gray=(r+g+b)/3
            # gray=g
            img[i, j] = [gray, gray, gray]

    img2 = cv2.resize(img, (1072, 1448))
    newname = os.path.join("kpw3", os.path.basename(pic_name) + ".png")
    print newname
    cv2.imwrite(newname, img2)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    if(not os.path.exists("./pic")):
        os.makedirs("pic")
    if(not os.path.exists("./kpw3")):
        os.makedirs("kpw3")

    for filename in glob.glob("./pic/*"):
        gepic(filename)
