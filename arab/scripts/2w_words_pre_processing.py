# Crop image from center
# remove whitespace
# convert to grayscale
# resize to 64X64

import cv2
import os
from os import path
from PIL import Image
from PIL import ImageOps
import imutils

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


input_dir_name = path.join("isolated_words_per_user")

for folder in os.listdir(input_dir_name):
    print(folder)
    input_dir = os.path.join(input_dir_name, folder)
    assert path.exists(input_dir)
    
    for file_name in os.listdir(input_dir):
        #print (file_name)
        image=Image.open(os.path.join(input_dir, file_name))
        image.load()
        imageSize = image.size
        
        # Crop center piece of the image containg the word
        cropped_image = crop_center(image, imageSize[0]-5, imageSize[1]-5)
        # Remove any whitespace surrounding the image        
        # remove alpha channel
        invert_im = cropped_image.convert("RGB")       
        # invert image (so that white is 0)
        invert_im = ImageOps.invert(invert_im)
        #invert_im.show()
        imageBox = invert_im.getbbox()
        
        cropped_image=cropped_image.crop(imageBox)
        #print ("%s Size:%s New Size:%s"%(file_name, imageSize, imageBox))
        cropped_image.save(os.path.join(input_dir, file_name))
   
    # for every file in the input dir, resize and convert to gray scale
    for file in os.listdir(input_dir):
        original_image = cv2.imread(os.path.join(input_dir,file))
        #cv2.imshow('original',original_image)
        gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        # resize image with aspect ratio maintained
        resized_img = imutils.resize(gray_image, height=128)
        #resized_img = cv2.resize(gray_image, (128,128), cv2.INTER_AREA)
        #cv2.imshow('resized', resized_img)
        cv2.imwrite(os.path.join(input_dir,file), resized_img)
