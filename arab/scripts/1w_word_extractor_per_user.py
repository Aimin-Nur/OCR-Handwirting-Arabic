import cv2
import os
from os import path

# Test Cropping
#image=cv2.imread(os.path.join(input_dirName, "1081_037.jpg"))
#cropped_image = image[680:900, 220:580]
#cv2.imshow("cropped", cropped_image)
#cv2.waitKey(5000)

def getWordName(page, column):
    if (page==1):
        if (column==0): return "azan"
        if (column==1): return "sakhar"
        if (column==2): return "mustadhafeen"
        if (column==3): return "abjadiyah"
        if (column==4): return "fasayakfeekahum"
    if (page==2):    
        if (column==0): return "ghazaal"
        if (column==1): return "ghaleez"
        if (column==2): return "qashtah"
        if (column==3): return "shateerah"
        if (column==4): return "mehras"

input_dir_name = path.join("raw_dataset")
output_dir_name = path.join("isolated_words_per_user")

# For each user process the images containig the letters
for userid in range(1,83):
    username="user" + format(userid,'03d')
    print(username)   
    output_dirName = os.path.join(output_dir_name, username)
    if (not os.path.exists(output_dirName)):
        os.makedirs(output_dirName)
    input_dirName = os.path.join(input_dir_name, username, "words")
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
        start_x = 215
        end_x = 605
        # Process each column
        for column in range(5):
            start_y = 680
            # Due to character size, some pages have higher initial height
            if (userid == 2): start_y = 665
            if (userid == 9): start_y = 690
            if (userid == 10 or userid == 11 or userid == 13): start_y = 670
            #print("(%d,%d,%d,%d)"%(start_x, start_y, end_x, start_y+height))
            word_name = getWordName(page, column)
            # Process each row within a column
            for row in range(10):
                #print("(%d,%d,%d,%d)"%(start_x, start_y, end_x, start_y+height))
                cropped_image = image[start_y:start_y+height, start_x:end_x]
                index = index + 1
                filename = "%s_%s_%s.png"%(username, word_name, format(index,'03d'))
                #cv2.imshow("cropped", cropped_image)
                cv2.imwrite(os.path.join(output_dirName, filename), cropped_image)
                start_y = start_y + height + y_increrment
            # Columns have different widths :(
            if (column == 0): start_x= 625; end_x = 1005
            if (column == 1): start_x= 1030; end_x = 1455
            if (column == 2): start_x= 1490; end_x = 1890
            if (column == 3): start_x= 1915; end_x = 2330

