# Write a function to return average (mean)of all values of digits using:
 #        a) mean function
  #       b) without mean function

  def average(alist):
  	return mean(alist)
  def mean_function(alist):
  	total = alist[0]
  	for i in range(len(alist)):
  		total = alist[i+1]+total
  	return sum/len(alist)
