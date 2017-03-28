print("Fizzbuzz counting up to 100.")
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    if num % 3 == 0:
        print("fizz")
    if num % 5 == 0:
        print("buzz")
    else:
        print(num)

