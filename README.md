# DBox
Drawing box tool for creating bounding boxes for detection 

## Requirments 
*python 3.5 
*Opencv 

## commands 

Read all images in the 'train.txt' file and show image after image 
*python3 dbox.py --dir train.txt

Show each image resized in a factor of 0.5
*python3 dbox.py --dir train.txt --fac 0.5 

Use yolo format for detection 
*python3 dbox.py --dir train.txt --fmt 1 

## Shortcuts
*[ENTER] save the bounding box to the directory 
*[=>] move to next image 
*[<=] move to previous image 
*[ESC] exit the drawing tool 
