''' write a  function that returns a random number between given values a and b'''
import random
def random(a,b):
	num = random.randint(a,b)
	return num

random_num = random(2,10)
print(random_num)


