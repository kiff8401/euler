#https://projecteuler.net/problem=6

import functools as fc;
import operator as op;
import math as m;

# really lame solution first, will think of a more mathematically 
# inclinded solution later
def getDifferenceOfSquares(n):
	numList = range(1,n+1) ;
	return m.pow(fc.reduce(op.add, numList, 0),2) - fc.reduce(op.add, [x*x for x in numList],0);



#test on 10
#print(getDifferenceOfSquares(10));

# and the final answer ...
print(getDifferenceOfSquares(100));