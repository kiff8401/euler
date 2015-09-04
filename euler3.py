import itertools as it;
import math as m


# just a test function which I thought might be needed to solve Euler3
# might be used with something else
def getListPrimeUpto(n):
	allnumbersTilln = range(2,n+1);
	while len(allnumbersTilln) > 0:
			p = allnumbersTilln[0] ;
			print(p);
			selectors = [x%p!=0 for x in allnumbersTilln];
			allnumbersTilln = list(it.compress(allnumbersTilln, selectors));

#getListPrimeUpto(30);

#Actual solution to Euler3
def returnMaxPrimeFactor(input):
	x = m.floor(m.sqrt(input));
	while(x>1):
		if(input%x == 0):
                        return max(returnMaxPrimeFactor(x), returnMaxPrimeFactor(input/x));
		else:
			x = x - 1;

	return input ; # input is a prime number



returnMaxPrimeFactor(600851475143);



