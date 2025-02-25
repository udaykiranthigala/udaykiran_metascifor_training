x=input("enter the string: ")
upper=x.upper()
lower=x.lower()
vowels="AEIOUaeiou"
count=0
for char in x:
    for char in vowels:
        count+=1

reverse=x[::-1]
print(upper)
print(lower)
print(reverse)
print("The vowels count is: ",count)