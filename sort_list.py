''' write a function to sort a given list and return sorted list using sort() or sorted() functions'''
def sorted_list(alist):
	return sorted(alist)
sorted_me = sorted_list([5,2,1,7,8,3,2,9,4])
print(sorted_me)
def sort_list(alist):
	return alist.sort()
sort_me = sort_list([5,2,1,7,8,3,2,9,4])
print(sort_me)
