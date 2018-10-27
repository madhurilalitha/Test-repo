#23) Write a function to return boolean if given number satisfies ANY of the below 3 conditions. If ALL conditions fail return False
#         a) x is divisible by 7
#         b) x > 70 and x <=100
 #        c) If x is positive 


def check_any_3_conditions(num):
 	cond1 = num%7
 	cond2 = num>70 and num<=100
 	cond3 = num>0
 	if cond1 == 0 or cond2 or cond3:
 		return True
 	else:
 		return False
check_conditions = check_any_3_conditions(77)
print(check_conditions)
