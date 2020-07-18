def SecondLowest(list1):
	list2 = []
	list1.sort(key=lambda x: x[1])
	l = len(list1)
	val = list1[0][1]
	for i in range(1,l):
		temp = list1[i][1]
		if temp > val:
			cval = temp
			break
	for i in range(1,l):
		ele = list1[i][1]
		if ele == cval :
			list2.append(list1[i][0])
	list2.sort()
	for i in list2:
		print(i)

list1 = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
SecondLowest(list1)