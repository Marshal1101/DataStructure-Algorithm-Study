## 11653 소인수분해 (구현)

import sys

N = int(sys.stdin.readline())

def prime_factorization(n):
	k = 2
	while n != 1 :
		if not n % k :
			n /= k
			print(k)
		else :
			k += 1  

prime_factorization(N)