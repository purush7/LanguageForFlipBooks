import library as lib
import os
import time
import numpy as np
import cv2
from fpdf import FPDF

white = [255,255,255]
pdf=FPDF()


butterflyPos1=lib._open( 'butterfly_pos1.jpg',20,20,0,white)
butterflyPos2=lib._open( 'butterfly_pos2.jpg',20,20,0,white)
back_ground=lib._open( 'back.jpeg',1000,1000,0,white)
page=lib._newPage( 1000,1000)
page=lib._addImage( page,back_ground,0,0)
rowPos=569
for i in range(0,1000,50):
	if (i%2 == 0):
		result_page=lib._addImage( page,butterflyPos1,rowPos,i)
		lib._write( 200,180,pdf,result_page,i)
	else:
		result_page=lib._addImage( page,butterflyPos2,rowPos,i)
		lib._write( 200,180,pdf,result_page,i)


lib._pdf( 'output2.pdf',pdf)
