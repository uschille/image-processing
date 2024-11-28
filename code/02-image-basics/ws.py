"""
 * Python program to create an image containing a single, white square.
 * The image is saved in two formats: bmp and jpg.
 *
 * usage: python ws.py <dim>
"""
import skimage.io
import sys
import numpy as np

dim = int(sys.argv[1])

img = np.zeros((dim, dim, 3), dtype="uint8")
img.fill(255)

skimage.io.imsave(fname="ws.bmp", arr=img)
skimage.io.imsave(fname="ws.jpg", arr=img)
