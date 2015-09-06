# https://projecteuler.net/problem=5
# Modified function from Euler4.py
import itertools as it;
import functools as fc;
import operator as op;
import math as m

def getListPrimeUpto(n):
    output = [];
    allnumbersTilln = range(2,n+1);
    while len(allnumbersTilln) > 0:
        p = allnumbersTilln[0] ;
        output.append(p);
        selectors = [x%p!=0 for x in allnumbersTilln];
        allnumbersTilln = list(it.compress(allnumbersTilln, selectors));
    return output;


def getMultiplyingFactor(num, allPrimes):
    for primeNumber in allPrimes:
        if(num%primeNumber == 0):
            return primeNumber;


# returns smallest number divisible by all  numbers from 1 to n
def smallestDivisiblebyAllUpto(n):
    originalList = range(1,n+1);
    allPrimes = getListPrimeUpto(n);

    # Concept of filtering# 
    otherNumbers = [x for x in originalList if x not in allPrimes];
    #print(otherNumbers);

    # reduce and  operator.mul concepts in python3
    result = fc.reduce(op.mul, allPrimes, 1);  # "initialize value"
    #print(result);

    # Try to express the following in a more pythonic way
    for num in otherNumbers:
        if(result%num != 0):
            result = result* getMultiplyingFactor(num, allPrimes);

    return result;

print(smallestDivisiblebyAllUpto(20));
