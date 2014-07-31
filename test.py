
import timeit


t = timeit.Timer("""
A= int(random.randint(2, 2**20))
factor.factor(A)
print bin(A)
""",
"""import factor
import random
""")

print 'TIMEIT:'
results  = t.repeat(50, 1)
print "fastest: " + str(min(results))
print "average: " + str(sum(results)/float(len(results)))


"""
A= int(random.randint(2, 2**30))
factor.factor(A)
"""

"""
bogosort.bogosort([1,2,3,4,5,6,7])
"""