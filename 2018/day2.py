from pylab import *

Lines = open('day2_input.txt').readlines()

Data = []
for Elements in Lines:
	Line = Elements.strip('\n')
 	Data.append(Line)

TwoTimes = 0
ThreeTimes = 0

for Lines in Data:
	CountedTwoCharacters=[]
	CountedThreeCharacters=[]
	for Character in Lines:
		if (Lines.count(Character)==2) and (len(CountedTwoCharacters)==0):
			TwoTimes+=1
			CountedTwoCharacters.append(Character)
		elif (Lines.count(Character)==3) and (len(CountedThreeCharacters)==0):
			ThreeTimes +=1
			CountedThreeCharacters.append(Character)
		else:
			pass

print(TwoTimes*ThreeTimes)
