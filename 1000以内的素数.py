def prime(n):
	for i in range(2,n):
		if n%i==0:
			return False
		if i==n-1:
			return True
output=filter(prime,range(2,1000))
print(list(output))
