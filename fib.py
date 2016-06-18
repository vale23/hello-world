import sys

n = int (sys.argv [1])

fib1 = 0
fib2 = 1
fib_sum = 0

if n == 1:
    fib_sum = 0
elif n == 2:
    fib_sum = 1
else:
	for count in range ( n-1):
		fib_sum = fib1 + fib2
		fib1 = fib2
  		fib2 = fib_sum
print(fib_sum)
