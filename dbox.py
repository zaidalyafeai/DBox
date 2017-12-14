import cv2
import numpy as np
import argparse
import os 

drawing = False # true if mouse is pressed
ix,iy = -1,-1
box = ''
def parser_opt():
	parser = argparse.ArgumentParser(description='Draw bounding boxes')
	parser.add_argument('--dir', type=str, help='text file containing directory of images')
	parser.add_argument('--fac', type=float, help='zoom in or out image factor')
	parser.add_argument('--fmt', type=float, help='Choose format of the box')
	return parser 

# mouse callback function
def draw_rectangle(event,x,y,flags,param):

	global ix,iy,drawing,img_res,img_cpy,f_x,f_y,box 

	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix,iy = x,y

	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
		    img_cpy = img_res.copy()
		    cv2.rectangle(img_cpy,(ix,iy),(x,y),(255,255,0),3)


	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		cv2.rectangle(img_cpy,(ix,iy),(x,y),(255,255,0),3)
		box = str(int(ix / f_x)) +' '+ str(int(iy / f_y)) +' '+ str(int((x-ix) / f_x))+ ' '+str(int((y-iy) / f_y))

def format(box, shape , f = 1):

	#yolo format 
	if f == 1:
		if box == '':
			return ''
		x,y,w,h = box.split(' ')
		x = float(x)
		y = float(y)
		w = float(w)
		h = float(h)
		H,W,_ = shape 
		return str((x+w/2)/W)+' '+str((y+h/2)/H)+' '+str(w/W)+' '+str(h/H)
	elif f == 0:
		return box 

def start(dirc , fact = 1.0):
	global ix,iy,drawing,img_res,img_cpy,f_x,f_y,box,fmt
	f_x = fact
	f_y = fact 
	indx = 1 
	with open(dirc,'r') as f:
		txtf = f.readlines()

	#remove next line characters
	for i in range(len(txtf)):
		txtf[i] = txtf[i].replace('\n','')

	#read first impage 
	im = cv2.imread(txtf[indx])
	img_res = cv2.resize(im.copy(), (0,0), fx=f_x, fy=f_y) 
	img_cpy = img_res.copy()

	#call back function 
	cv2.namedWindow('image')
	cv2.setMouseCallback('image',draw_rectangle)

	while(1):
		#show current image 
		cv2.imshow('image',img_cpy)

		#wait for key press
		k = cv2.waitKeyEx(1) & 0xFF

		#if k!= 255:
		#	print(k)

		#use [ENTER] to save current bounding box 
		if k == 13:
			curr_txt = txtf[indx]
			dot_ind = curr_txt.find('.')
			txt = curr_txt[:dot_ind]+'.txt'
			with open(txt,'w') as f:
				f.write(format(box,im.shape,f=fmt))
			print('saving to ',txt)

		#use [=>] to move to next image 
		if k == 109:

			if indx +1 < len(txtf):
				indx+=1
				im = cv2.imread(txtf[indx])
				img_res = cv2.resize(im.copy(), (0,0), fx=f_x, fy=f_y) 
				img_cpy = img_res.copy()
				box =''
				print('Processing next image ')
			else:
				print('No next image')

		#use [<=] to move to previous image 
		if k == 110:
			if indx -1 >= 0 :
				indx-=1
				im = cv2.imread(txtf[indx])
				img_res = cv2.resize(im.copy(), (0,0), fx=f_x, fy=f_y) 
				img_cpy = img_res.copy()
				box=''
				print('Processing previous image ')
			else:
				print('no previous image')
		#use [ESC] to exit
		if k == 27:
			break
		
	cv2.destroyAllWindows()

#get parser arguments
parser = parser_opt()
args = parser.parse_args()
dirc = args.dir
f = args.fac
fmt = args.fmt 

#check if format is checked 
if fmt == None:
	fmt = 0 

#check if resize options are given 
if f is not None:
	start(dirc,fact = f)
else:
	start(dirc)





