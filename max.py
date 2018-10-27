''' Write a function to get maximum element from a list of digits?
	a) using max() function
	b) using without max() function
'''
alist= [2,4,1,3,1,5]
max(alist)

#without max()
sorted_list = alist.sort()
max_num = sorted_list.pop()

