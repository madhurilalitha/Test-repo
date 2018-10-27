#  Given a list and a num. Write a function to return boolean if that element is not in the list.

def check_num_in_list(alist, num):
	for i in alist:
		if num in alist and num%2 != 0: 
			return True
		else:
			return False
sample = check_num_in_list([2,7,3,1,6,9], 6)
print(sample)




