import sys

try:
    n = int(sys.argv[1])
except IndexError:
    n = int(input("Choose a number to fizzbuzz up to: "))

print("Fizzbuzz counting up to {}. ".format(n))
for num in range(1, n + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    if num % 3 == 0:
        print("fizz")
    if num % 5 == 0:
        print("buzz")
    else:
        print(num)
