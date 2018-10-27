''' write a function that prints the elements of the list with two places skipped '''
def print_nums(alist):
	temp = []
	for i in range(0, len(alist), 2):
		temp.append(alist[i])
        return temp
newlist = print_nums([2,4,1,6,7,4,9,32])
print(newlist)
