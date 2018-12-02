from pylab import *

Lines = open('day1_input.txt').readlines()

Data = []

for Elements in Lines:
	Line = Elements.strip('\n')
	Data.append(int(Line))

FinalSum = sum(Data)


print FinalSum

#Part 2

Inlist = False
Count = 0
Frequency = [0]

def CheckFrequency(Frequency,Data, Inlist, Count):
	for i in range (len(Data)):
		NewFrequency = Data[i]+Frequency[-1]
		if NewFrequency in Frequency:
			print("Frequency = %.f" % NewFrequency)
			Inlist = True
			break
		elif i == (len(Data)-1):
			Frequency.append(NewFrequency)
			Count += 1
			print('Count = %.f' % Count)
		else:
			 Frequency.append(NewFrequency)
	return Inlist, Count

while Inlist == False:
	Inlist, Count = CheckFrequency(Frequency ,Data, Inlist, Count)

