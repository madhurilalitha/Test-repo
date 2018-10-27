#Given two lists,, list1 and list2. If you encounter if the elements are same at any index then take that element and return the square of the number. Implement this a) with break b) with return
#Ref: https://stackoverflow.com/questions/189645/how-to-break-out-of-multiple-loops-in-python (4rth answer)
#Hint: Use two for loops
def print_matched_elements():
	for a in xrange(10):
		for b in xrange(20):
			if a == b:
				print(a*a)
				break
sample = print_matched_elements()
print(sample)



