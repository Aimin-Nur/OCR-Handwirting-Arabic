import cv2
import os
from os import path

# Test Cropping
#image=cv2.imread(os.path.join(input_dirName, "1081_037.jpg"))
#cropped_image = image[680:900, 220:580]
#cv2.imshow("cropped", cropped_image)
#cv2.waitKey(5000)

def getParagraphName(page):
    if (page==1):
        return "paragraph_1"
    if (page==2):    
        return "paragraph_2"
    if (page==3):    
        return "paragraph_3"

input_dir_name = path.join("raw_dataset")
output_dir_name = path.join("paragraphs_per_user")

# For each user process the images containig the letters
for userid in range(1,83):
    username="user" + format(userid,'03d')
    print(username)   
    output_dirName = os.path.join(output_dir_name, username)
    if (not os.path.exists(output_dirName)):
        os.makedirs(output_dirName)
    input_dirName = os.path.join(input_dir_name, username, "sentences")
    #width = 390
    #x_increment = 20
    height = 216
    y_increrment = 20
    page = 0
    # Process all the user files
    for file in os.listdir(input_dirName):
        print(file)
        image=cv2.imread(os.path.join(input_dirName, file))
        page = page + 1
        #if (page == 2): break
        index = 0
        if (page == 1):
            start_x = 305
            end_x = 2140
            start_y = 1305
            height = 1695
        if (page == 2):
            start_x = 310
            end_x = 2140
            start_y = 1390
            height = 1610
        if (page == 3):
            start_x = 305
            end_x = 2140
            start_y = 935
            height = 1565
            
        paragraph_name = getParagraphName(page)
        # Process each row within a column
        cropped_image = image[start_y:start_y+height, start_x:end_x]
        index = index + 1
        filename = "%s_%s_%s.png"%(username, paragraph_name, format(index,'03d'))
                #cv2.imshow("cropped", cropped_image)
        cv2.imwrite(os.path.join(output_dirName, filename), cropped_image)

