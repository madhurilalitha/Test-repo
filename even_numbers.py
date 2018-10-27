'''  write a function that takes three lists and returns a new list where all three lists are added'''
def even(alist):
	evenlist = []
	for num in alist:
		if num%2 == 0:
			evenlist.append(num)
	return evenlist
evens = even([2,5,3,6])
print(evens)
