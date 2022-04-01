import numpy as np
from imageio import imread, imwrite
import cv2

img = imread('yaztem.png')

arr = img + np.array( [0.1, 0.2, 0.5])

arr2 = (255*arr/arr.max().astype(np.uint8)

imwrite('yaztem.png', arr2)

