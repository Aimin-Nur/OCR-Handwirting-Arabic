import cv2
import os
from os import path

# Test Cropping
#image=cv2.imread(os.path.join(input_dirName, "1081_037.jpg"))
#cropped_image = image[680:900, 220:580]
#cv2.imshow("cropped", cropped_image)
#cv2.waitKey(5000)

def getLetterName(page, column):
    if (page==1):
        if (column==0): return "beh_middle"
        if (column==1): return "beh_begin"
        if (column==2): return "beh_regular"
        if (column==3): return "alif_end"
        if (column==4): return "alif_regular"
    if (page==2):    
        if (column==0): return "jeem_end"
        if (column==1): return "jeem_middle"
        if (column==2): return "jeem_begin"
        if (column==3): return "jeem_regular"
        if (column==4): return "beh_end"
    if (page==3):    
        if (column==0): return "seen_regular"
        if (column==1): return "raa_end"
        if (column==2): return "raa_regular"
        if (column==3): return "dal_end"
        if (column==4): return "dal_regular"
    if (page==4):    
        if (column==0): return "sad_begin"
        if (column==1): return "sad_regular"
        if (column==2): return "seen_end"
        if (column==3): return "seen_middle"
        if (column==4): return "seen_begin"
    if (page==5):    
        if (column==0): return "tah_end"
        if (column==1): return "tah_middle"
        if (column==2): return "tah_regular"
        if (column==3): return "sad_end"
        if (column==4): return "sad_middle"
    if (page==6):    
        if (column==0): return "feh_regular"
        if (column==1): return "ain_end"
        if (column==2): return "ain_middle"
        if (column==3): return "ain_begin"
        if (column==4): return "ain_regular"
    if (page==7):    
        if (column==0): return "qaf_begin"
        if (column==1): return "qaf_regular"
        if (column==2): return "feh_end"
        if (column==3): return "feh_middle"
        if (column==4): return "feh_begin"
    if (page==8):    
        if (column==0): return "kaf_middle"
        if (column==1): return "kaf_begin"
        if (column==2): return "kaf_regular"
        if (column==3): return "qaf_end"
        if (column==4): return "qaf_middle"
    if (page==9):    
        if (column==0): return "lam_end"
        if (column==1): return "lam_middle"
        if (column==2): return "lam_begin"
        if (column==3): return "lam_regular"
        if (column==4): return "kaf_end"
    if (page==10):    
        if (column==0): return "noon_regular"
        if (column==1): return "meem_end"
        if (column==2): return "meem_middle"
        if (column==3): return "meem_begin"
        if (column==4): return "meem_regular"
    if (page==11):    
        if (column==0): return "heh_begin"
        if (column==1): return "heh_regular"
        if (column==2): return "noon_end"
        if (column==3): return "noon_middle"
        if (column==4): return "noon_begin"
    if (page==12):    
        if (column==0): return "yaa_regular"
        if (column==1): return "waw_end"
        if (column==2): return "waw_regular"
        if (column==3): return "heh_end"
        if (column==4): return "heh_middle"
    if (page==13):    
        if (column==0): return "lam_alif"
        if (column==1): return "alif_hamza"
        if (column==2): return "yaa_end"
        if (column==3): return "yaa_middle"
        if (column==4): return "yaa_begin"

input_dir_name = path.join("raw_dataset")
output_dir_name = path.join("isolated_alphabets_per_user")

# For each user process the images containig the letters
for userid in range(1,83):
    username="user" + format(userid,'03d')
    print(username)   
    output_dirName = os.path.join(output_dir_name, username)
    if (not os.path.exists(output_dirName)):
        os.makedirs(output_dirName)
    input_dirName = os.path.join(input_dir_name, username, "letters")
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
            if (page == 7 or page == 9): start_y = 695
            #print("(%d,%d,%d,%d)"%(start_x, start_y, end_x, start_y+height))
            letter_name = getLetterName(page, column)
            # Process each row within a column
            for row in range(10):
                #print("(%d,%d,%d,%d)"%(start_x, start_y, end_x, start_y+height))
                cropped_image = image[start_y:start_y+height, start_x:end_x]
                index = index + 1
                filename = "%s_%s_%s.png"%(username, letter_name, format(index,'03d'))
                #cv2.imshow("cropped", cropped_image)
                cv2.imwrite(os.path.join(output_dirName, filename), cropped_image)
                start_y = start_y + height + y_increrment
            # Columns have different widths :(
            if (column == 0): start_x= 625; end_x = 1005
            if (column == 1): start_x= 1030; end_x = 1455
            if (column == 2): start_x= 1490; end_x = 1890
            if (column == 3): start_x= 1915; end_x = 2330

