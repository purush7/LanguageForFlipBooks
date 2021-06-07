import cv2
import numpy  as np
from fpdf import FPDF
import os
import time

white = [255,255,255]



def _open(file , finalRows, finalCols, flag , background):

    im = cv2.imread(file)

    rows = im.shape[0]
    cols = im.shape[1]

    for col in range(cols):                                             #  make the white pixels to the primary background
        for row in range(rows):
            if (im[row,col] == background).all():
                im[row,col] = white

    if flag==1:
        im = np.flip(im,axis=1)                                             #  for reversing the image along horizontal axis

    im = cv2.resize(im,dsize =(finalCols,finalRows))

    return im

def _addImage(page , im , rowPos, colPos):
    inputPage = page.copy()
    for row in  range(im.shape[0]):
        if row+rowPos >= inputPage.shape[0]:
            break
        for col in range(im.shape[1]):
            if col+colPos >= inputPage.shape[1]:
                break
            elif not (im[row,col]== white).all():
                inputPage[row+rowPos,col+colPos] = im[row,col]
    return inputPage

def _write(width,height,pdf,resultPage,pgno):
    file = 'output'+str(pgno)+'.png'
    cv2.imwrite(file,resultPage)
    pdf.add_page()
    pdf.image(file,0,0, width,height)
    os.remove(file)

def _newPage(rows,cols):
    page = np.zeros((rows,cols,3))
    page[:,:,0] = 255
    page[:,:,1] = 255
    page[:,:,2] = 255
    return page

def _pdf(file,pdf):
    pdf.output(file,'F')

