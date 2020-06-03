# Assign values
individual_time={'A':1, 'B':2, 'C':7, 'D':10}
totalTime = 20
timeSpend = 0
#now sort time values from dictionary 
orderTime = list(individual_time.values())
orderTime.sort()

# using the sorted values list to sort keys 
# and assign them to person variables
for i, j in individual_time.items():
	if j== orderTime[3]:
		p4 = i
	elif j== orderTime[2]:
		p3 = i
	elif j== orderTime[1]:
		p2 = i
	elif j== orderTime[0]:
		p1 = i
print('\n A,B,C,D all are on left side. \n')
print('First person ' + p1 + ' and ' + p2 + ' will cross by spending ' + str(orderTime[1]) + ' min of total ' + str(totalTime) + ' min.')
timeSpend += orderTime[1]
print('Then person ' + p1 + ' will return spending ' + str(orderTime[0]) + ' over ' + str(timeSpend) + ' min already spent.')
timeSpend += orderTime[0]
print('Now person ' + p3 + ' and ' + p4 + ' cross the bridge spending ' + str(orderTime[3]) + ' more min over ' + str(timeSpend) + ' total spent time.')
timeSpend += orderTime[3]
print('Now person ' + p2 + ' returns to get person ' + p1 + ' spending ' + str(orderTime[1]) + ' more min, over ' + str(timeSpend) + ' already spent.')
timeSpend += orderTime[1]
print('Finally person ' + p1 + ' and ' + p2 + ' join their friends on the other side, spending another ' + str(orderTime[1]) + ' min and if we add that to ' + str(timeSpend) + ' min already spend, that makes it ' + str(timeSpend+orderTime[1]) + ' min in total.')
print('\n Now A,B,C,D all persons are on right side of Bridge.\n')
