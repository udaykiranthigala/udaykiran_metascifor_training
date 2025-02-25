x = int(input("Enter a positive integer: "))

if x == 0:
    print("The number is neither even nor odd.")
elif x % 2 == 0:
    print("The %d is an even number." % x)
else:
    print("The %d is an odd number." % x)
