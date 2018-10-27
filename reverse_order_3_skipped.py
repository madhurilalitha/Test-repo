'''write a function that prints values in reverse way but with three positions skipped'''
def reverse_3_skip(alist):
	temp_list = []
	for i in range(len(alist)-1, 0, 3):
		temp_list.append(alist[i])
	return temp_list
reverse = reverse_3_skip([4,2,5,3,6,1,2,6,8,6,9])
print(reverse)