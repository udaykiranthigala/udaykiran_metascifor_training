def fact(n):
    if n < 0:
        return "Factorial is not available for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
x = int(input("Enter a number: "))
print(f"The factorial of {x} is {fact(x)}")
