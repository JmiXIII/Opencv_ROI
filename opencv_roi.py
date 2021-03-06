# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:05:14 2017

@author: user11
"""

import cv2
import numpy as np

if __name__ == '__main__' :

    # Read image
    im = cv2.imread("1.jpg")

    # Select ROI
    fromCenter = False
    r = cv2.selectROI("Image", im, fromCenter)

    # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    # Display cropped image
    cv2.imshow("Image", imCrop)
    cv2.waitKey(0)