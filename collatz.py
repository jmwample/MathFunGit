import random

def repeat(num):
	test = int(num)
	steps = 0
	while test != 1:
		#print test
		if (test % 2 == 1):
			test *= 3
			test += 1
		else:
			test /= 2
		steps += 1
	print str(steps) + " steps"

#repeat(random.randint(2, 2**20))
