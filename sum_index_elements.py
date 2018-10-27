# Given two lists of equal sizes, sum all the corresponding index elements and return a new list.
#	Lis1 = [1,2,3,4,5] List2=[6,7,8,9,0]
#	new list output = [7, 9, 11,13,5]

def sum_index_elements(alist, blist):
	new_list = []
	for a in range(len(alist)):
		new_list.append(alist[a]+blist[a])
	return new_list
test_code = sum_index_elements([2,3,1,4,2], [1,4,2,4,2])
print(test_code)

