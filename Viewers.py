#!/usr/bin/env python
# coding: utf-8
# %matplotlib notebook
import matplotlib.pyplot as plt
import skimage.io
image = skimage.io.imread(fname="code/03-skimage-images/chair.jpg")
skimage.io.imshow(image)
plt.show()

import hyperspy.api as hs
img = hs.load("code/02-image-basics/tree.jpg")
image = skimage.io.imread("code/02-image-basics/tree.jpg")
img = hs.signals.Signal2D(image.view(dtype=[('R', 'u1'), ('G', 'u1'), ('B', 'u1')]).reshape(image.shape[:-1]))
img.plot()
plt.show()

# %gui qt
import napari
image = skimage.io.imread("code/02-image-basics/tree.jpg")
viewer = napari.view_image(image)
napari.utils.nbscreenshot(viewer)
