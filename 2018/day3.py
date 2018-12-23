from pylab import *

Lines = open('day3_input.txt').readlines()

Data = []

for Elements in Lines:
	Element = Elements.replace('\n', '')
	Data.append(Element.split(' '))

XStart = []
YStart = []
XSize = []
YSize = []
XSqaure = []
YSquare = []
Line = []
for i in range(len(Data)):
	start = Data[i][2].replace(':','').split(',')
	size = Data[i][3].split('x')
	line = Data[i][0].replace('#','')
	

	XStart.append(int(start[0]))
	YStart.append(int(start[1]))
	XSize.append(int(size[0]))
	YSize.append(int(size[1]))
	Line.append(int(line))
	
	squarex = int(start[0]) + int(size[0])
	squarey = int(start[1]) + int(size[1])
	XSqaure.append(squarex)
	YSquare.append(squarey)

MaxX = max(XSqaure)
MaxY = max(YSquare)

Matrix = zeros((MaxX,MaxY))

for i in range(len(XStart)):
	Matrix[XStart[i]:(XStart[i]+XSize[i]),YStart[i]:(YStart[i]+YSize[i])]+=1
	
Count = 0

for Lines in Matrix:
	for Elements in Lines:
		if Elements >= 2:
			Count +=1
		else:
			pass
print Count

# part two

for i in range(len(XStart)):
	square = Matrix[XStart[i]:(XStart[i]+XSize[i]),YStart[i]:(YStart[i]+YSize[i])]
	if 1 in square and 2 not in square:
		print i+1
