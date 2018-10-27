def add_3_lists(alist, blist, clist):
	final_list = alist.extend(blist)
	final_list.extend(clist)
	return final_list
sample = add_3_lists([1,2], [3,4], [5,6])
print(sample)
