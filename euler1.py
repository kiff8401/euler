result = 0;

# try to do this using lambda expressions please?

for i in range(1000):
	if(i%3 == 0 or i%5 == 0):
		result = result + i;

print(result)