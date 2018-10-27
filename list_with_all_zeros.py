#Write a function to initialze a list of size 100 with all values as 0s.
 #     Ex: [0,0,0,0,0,0,0,0,0.......]
def initialize_list():
	return [0 for i in range(101)]
		
sample = initialize_list()
print(sample)

