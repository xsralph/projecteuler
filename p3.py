import sys

def largestprime(n):
	#print n
	if n == 1: return 0
	if (n % 2) == 0: return max(2,largestprime(n/2))
	if (n ** 0.5) < 4.0: return n
	for i in range(3,int( n ** (0.5))):
		if (n % i) == 0: return max(i, largestprime(n/i))
	return n

print largestprime(int(sys.argv[1]))
