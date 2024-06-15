# This script is used to pre-process the alphabets 
# (remove surrounding whitespace, resize (with aspect ratio), grayscale)
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

#input_dir_name = path.join("isolated_alphabets_per_alphabet")
input_dir_name = path.join("isolated_alphabets_per_user")

for folder in os.listdir(input_dir_name):
    print(folder)
    input_dir = os.path.join(input_dir_name, folder)
    # for every file in input directory, crop from center and remove border
    for file_name in os.listdir(input_dir):
        #print (file_name)
        image=Image.open(os.path.join(input_dir, file_name))
        image.load()
        imageSize = image.size
        # Crop center piece of the image containg the letter 
        # eliminating 5 pixels on sides to remove border lines
        #image = crop_center(image, 300, 180)
        image = crop_center(image, imageSize[0]-20, imageSize[1]-20)
        #image.save(os.path.join(input_dir, file_name))
        
        # Remove any whitespace surrounding the image      
        # remove alpha channel
        invert_im = image.convert("RGB") 
        
        # invert image (so that white is 0)
        invert_im = ImageOps.invert(invert_im)
        #invert_im.show()

        imageBox = invert_im.getbbox()
        
        cropped=image.crop(imageBox)
        #print ("%s Size:%s New Size:%s"%(file_name, imageSize, imageBox))
        # only save cropped image if it is not less than 64X64
        # otherwise keep original image
        cropped_width, cropped_height = cropped.size
        if (cropped_width>64 and cropped_height>64):
            cropped.save(os.path.join(input_dir, file_name))
        else:
            image.save(os.path.join(input_dir, file_name))
        
    # for every file in the input dir, resize and convert to gray scale
    for file in os.listdir(input_dir):
        original_image = cv2.imread(os.path.join(input_dir,file))
        #cv2.imshow('original',original_image)
        # convert image to grayscale
        gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        # resize image with aspect ratio maintained
        resized_img = imutils.resize(gray_image, height=128)
        #resized_img = cv2.resize(gray_image, (64,64), cv2.INTER_LINEAR)
        #cv2.imshow('resized', resized_img)
        cv2.imwrite(os.path.join(input_dir,file), resized_img)
        