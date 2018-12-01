from pylab import *

lines = open('day1_input.txt').readlines()

data = []
FinalSum = 0

for elements in lines:
	line = elements.strip('\n')
	data.append(int(line))

for element in data:
	FinalSum+=element

print FinalSum