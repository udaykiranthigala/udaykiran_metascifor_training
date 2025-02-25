print("Prime numbers between 1 and 50 are:")

for x in range(1, 51):
    if x > 1:
        is_prime = True  
        for i in range(2, x):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            print(x, end=" ")
