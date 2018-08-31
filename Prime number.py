# Program to find out the prime numbers from the range of numbers given by user

# solution 1

number = int(input("Enter range: "))

for x in range(2, number + 1):
    isPrime = True
    for y in range(2, x):
        if x % y == 0:
           isPrime = False

    if isPrime:
        print(x, "is a prime number")


#num1 = int(input("Enter number range: "))

# solution 2

for i in range(2, 12):
    j = 2
    counter = 0
    while(j < i):
        print("i is: ", i)
        print("j is:", j)
        if i % j == 0:
           counter+=1
           j+=1
        else:
           j+=1
    if counter == 0:
        print(i, "is prime")
    else:
        counter = 0

