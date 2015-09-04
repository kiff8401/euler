def evenFebSum():
	a, b = 0, 1
	sum = 0;
	limit = 4000000;
	while a <= limit:
	    if a%2 == 0:
	    	sum = sum + a 
	    a,b = b,a+b 
	return sum;


result = evenFebSum();

print(result)
