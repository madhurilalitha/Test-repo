'''given a list print all the elements of the list in reverse way'''
def reverse_order(alist):
	reverse_list = []
	for i in range(len(alist)-1, -1):
		reverse_list.append(alist[i])
	return reverse_list
reverse = reverse_order([2,6,0,1,5])
print(reverse)
	
