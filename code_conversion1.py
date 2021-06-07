import library as lib
import os
import time
import numpy as np
import cv2
from fpdf import FPDF

white = [255,255,255]
pdf=FPDF()


back_ground=[247,247,247]
car=lib._open( 'car.png',100,100,1,white)
tree=lib._open( 'tree.png',250,200,0,back_ground)
back_ground=lib._open( 'back.jpeg',1000,1000,0,white)
page=lib._newPage( 1000,1000)
page=lib._addImage( page,back_ground,0,0)
rowPos=569
page=lib._addImage( page,tree,rowPos,400)
rowPos=899
for pgno in range(0,1000,50):
	resultPage=lib._addImage( page,car,rowPos,pgno)
	lib._write( 200,180,pdf,resultPage,pgno)

lib._pdf( 'output.pdf',pdf)
