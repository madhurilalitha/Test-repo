''' write a function that pops all elements at even indexes
'''
def pop_elements(alist):
	for i in range(0, len(alist)):
		if i%2 == 0:
			alist.pop(i)
	return alist
