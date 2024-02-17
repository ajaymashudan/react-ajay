def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False 
        return num

x = int(input("Enter a number"))
result = prime(x)
print(result," is a prime number ")