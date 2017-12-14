# DBox
Drawing box tool for creating bounding boxes for detection. It also supports YOLO formatting by setting the flag fmt to 1  

![Alt text](img1.jpg?raw=true "Title")
## Requirments 
* python 3.5 
* Opencv 

## commands 

Read all images in the 'train.txt' file and show image after image 
* python3 dbox.py --dir train.txt

Show each image resized in a factor of 0.5
* python3 dbox.py --dir train.txt --fac 0.5 

Use YOLO format for detection 
* python3 dbox.py --dir train.txt --fmt 1 

## Shortcuts
* [ENTER] save the bounding box to the directory 
* [m] move to next image 
* [n] move to previous image 
* [ESC] exit the drawing tool 
