# Given a list of booleans, return True if all the boolean values of the list are False
#	List = [False, False, False] output: True
#	a) using if all()
#           b) without using if all()

def check_if_all_false(alist):
	for i in alist:
		if i == 'False':
			return True

test = check_if_all_false([False, False])
print(test)
