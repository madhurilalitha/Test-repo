#Write a function to print all elements in a list but skipping the indices if index is odd
#	Hint : Use continue for skipping iterations

def skip_odd_index_nums(alist):
	temp=[]
	for i in range(len(alist)):
		if i%2 != 0:
			temp.append(alist[i])
	return temp
sample = skip_odd_index_nums([2,3,1,3,45,63,12])
print(sample)
