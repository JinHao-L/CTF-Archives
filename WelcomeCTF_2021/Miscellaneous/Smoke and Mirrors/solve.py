#coding: utf-8
import base64
from pathlib import WindowsPath
import PIL
from PIL import Image
import requests
from io import BytesIO
from PIL import ImageFilter
from PIL import ImageEnhance
import numpy as np

image = Image.open("image.png")

extracted = ''

pixels = image.load()
# Iterate over pixels of the first row
pixel_counter = 0
for y in range(0, image.height):
    if pixel_counter == 91136: break
    for x in range(0, image.width):
        pixel_counter = pixel_counter + 1
        if pixel_counter == 91136: break

        p = image.getpixel((x,y))
        # Store LSB of each color channel of each pixel
        extracted += bin(p)[-1]
        # print(bin(p))


# 91136 is for the flag length, 11392 * 8

f = open("out.txt", "w")
f.write(extracted)