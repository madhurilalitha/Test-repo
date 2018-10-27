# Write a function to return boolean if the list is empty?
#	a) using None
#           b) using len()
def check_if_empty_list(alist):
	#if alist is None:

	if len(alist) == 0:
		return True
	else:
		return False
check = check_if_empty_list([2,3])
print(check)
