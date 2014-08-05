"""
Sieve of Eratosthenes
One method, called the Sieve of Eratosthenes, of computing all of the prime
numbers less than a certain fixed positive integer N is to list all of the
numbers n such that 1 < n < N. Begin by eliminating all of the multiples
of 2. Next eliminate all of the multiples of 3. Notice that 4 has already been
crossed out. Now eliminate all of the multiples of 5. Notice that 6 has
already been crossed out, so now eliminate all multiples of 7. Continue in
this manner, until you reach the square root of N.
"""

import math
import sys

def erat_sieve(num):
	num_list = range(2, num+1)
	roof = math.sqrt(float(num))
	i =2
	while i <= roof:
		x = 2
		while (i*x) <= num :
			if (i*x) in num_list:
				num_list.remove(i*x)
			x+=1
		i+=1
	print num_list
	print str(len(num_list)) + " elements"

erat_sieve(int(sys.argv[1]))