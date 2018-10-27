#insert value 0 at indices where the index value is a 3 multiple
def insert_at_3_multiples(alist):
	for i in range(3, len(alist), 3):
		alist.insert(i, 0)
	return alist

		