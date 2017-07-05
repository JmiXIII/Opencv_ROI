# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 15:09:40 2017

@author: user11
"""

from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog
import cv2
import pytesseract

# Choose file
path = tkinter.filedialog.askopenfilename()

# Read image
im = cv2.imread(path)

# Select ROI
r = cv2.selectROI("Image", im, fromCenter = False)

# Crop image
imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

# Convert image to PIL
image = cv2.cvtColor(imCrop, cv2.COLOR_BGR2RGB)
image = Image.fromarray(image)

# Display cropped image
cv2.imshow("Image", imCrop)
cv2.imshow("Origin",im)
txt = pytesseract.image_to_string(image)
print(txt)
cv2.waitKey(0)