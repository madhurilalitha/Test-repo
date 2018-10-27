''' Given a list of digits print all values at odd indexes'''
def odd(alist):
	odd_index_list = []
	for i in range(len(alist)):
		if alist[i]%2 != 0:
			odd_index_list.append(i)
	return odd_index_list
odd_index = odd([1,5,7,2,4])
print(odd_index)
