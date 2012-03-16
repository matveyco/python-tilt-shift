import Image
import sys
import numpy as np
from scipy import ndimage
import ImageEnhance
from mask import mask

# INIT
blur_size = 4
image_base = "/Users/Mango/Desktop/tiltshift_alpha.png"
image_output = "/Users/Mango/Desktop/tiltshift_preview.png"

# LOAD
im_base = Image.open(image_base)
im_mask = mask.draw_mask(0,640,480,53,17,9,9)
im_mask = im_mask.resize(im_base.size)

# PROCESS
enh = ImageEnhance.Color(im_base)
im_base = enh.enhance(1.9)
enh = ImageEnhance.Contrast(im_base)
im_base = enh.enhance(1.4)

im_blurred = np.array(im_base, dtype=float)
im_blurred = ndimage.gaussian_filter(im_blurred, sigma=[blur_size,blur_size,0])
im_blurred = Image.fromarray(np.uint8(im_blurred))
im_base = im_base.convert("RGBA")

# MERGE AND SAVE
im_base.paste(im_blurred,mask=im_mask)
im_base.save(image_output)
