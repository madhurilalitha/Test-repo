#22) Write a function to return boolean if given number satisfies ALL of the below 3 conditions. 
  #       a) 10< x < 20
   #      b) x is odd
    #     c) last digit of x is multiple of 5

def check_all_conditions(num):
	con1 = num>10 and num<20
	con2 = (num%2) 
	con3 = (num%10) 
	if con1 and con2 != 0 and (con3 == 5 or con3 == 0):
		return True
	else:
		return False
check_all = check_all_conditions(13)
print(check_all)
