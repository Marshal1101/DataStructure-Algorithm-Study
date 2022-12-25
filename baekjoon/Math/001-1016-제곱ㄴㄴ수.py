import sys


def get_square_check(start, end):
    count = end - start + 1
    sieve = [False] * count
    
    for i in range(2, int(end**0.5+1)):
        square = i ** 2
        for j in range(((start-1)//square+1)*square, end+1, square):
            if not sieve[j-start]:
                sieve[j-start] = True
                count -= 1
    
    return count

start, end = map(int, sys.stdin.readline().split())
print(get_square_check(start, end))