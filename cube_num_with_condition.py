#Write a function to perform cube of an element if you encounter value 5 in a given list of a list of size 'n' :
 #    Arguments: Given list = ['a', ',b', 5, 10,34, 56]
 #    Hint: use 'break' if you encounter 5. For cubing refer pow() function from import math or do x*x*x


def cube_num_5(alist):
	for num in alist:
		if num == 5:
			print (num*num*num)
			break
sample = cube_num_5(['a', 'b', 5, 10,34, 56])
print(sample)



