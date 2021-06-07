import re
import sys
import os ,stat, subprocess

input_file = sys.argv[1]

outputFile = open("output.py",'w')
outputFile.write("import library as lib\nimport os\nimport time\nimport numpy as np\nimport cv2\nfrom fpdf import FPDF\n\n")
outputFile.write("white = [255,255,255]\npdf=FPDF()\n\n\n")

inputFile = open(input_file,'r')
lines  = inputFile.readlines()

tabs =0

def ifBlock(line, outputFile):
    pos = line.find(";",0,len(line))
    line =line[2:pos]
    outputFile.write(tabs*'\t'+"if"+line+':\n')
    

def forBlock(line, outputFile):
    pos = line.find(";",0,len(line))
    line =line[4:pos]
    listOfSublines = re.split(',',line)
    variable =  listOfSublines[0]
    pages = listOfSublines[1]
    iterationCount = listOfSublines[2]
    outputFile.write(tabs*'\t'+'for '+variable+" in range(0,"+pages+","+iterationCount+"):\n")

def elseBlock(line, outputFile):
    outputFile.write((tabs-1)*'\t'+'else:\n')

def endBlock(line, outputFile):
    outputFile.write("\n")

def statement(line, outputFile):
    flag =0
    pos = line.find(";",0,len(line))
    line =line[:pos]
    listOfSublines = re.split(' |\(|\)',line)
    outputFile.write(tabs*'\t')
    for elements in listOfSublines:
        if(len(elements)!=0 and elements[0]=='_'):
            flag=1
            outputFile.write("lib."+elements+"( ")
        else:
            outputFile.write(elements)
    if flag==1:
        outputFile.write(")")
    outputFile.write("\n")


for line in lines:
    if line[0]=='I':
        ifBlock(line,outputFile)
        tabs+=1
    elif line[0] == 'F':
        forBlock(line,outputFile)
        tabs+=1
    elif line[0] == 'E' and line[1] == 'l':
        elseBlock(line,outputFile)
    elif line[0] =='E':
        endBlock(line,outputFile)
        tabs-=1
    elif (line[0]=='_') or (line[0] >= 'a' and line[0] <= 'z'):
        statement(line,outputFile)

outputFile.close()
inputFile.close()

os.chmod('output.py',0o777)
os.system('python3 output.py')
os.remove('output.py')