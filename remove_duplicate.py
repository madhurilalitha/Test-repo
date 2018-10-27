''' write a function to remove a first occurence of a given value from list

'''
def remove_duplicate(alist):
	empty_list = []
	for num in alist:
		if num not in empty_list:
			empty_list.append(num)
    return empty_list
