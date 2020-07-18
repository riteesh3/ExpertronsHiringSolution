n1 = int(input("Enter number of elements in list1: "))
n2 = int(input("Enter number of elements in list2: ")) 
list1 = list(input("\nEnter the list1 elements: ").strip().split())[:n1]
list2 = list(input("\nEnter the list2 elements: ").strip().split())[:n2]
result = list1
for ele in list2:
	if ele in result:
		result.remove(ele)
	else:
		result.append(ele)
print(result)