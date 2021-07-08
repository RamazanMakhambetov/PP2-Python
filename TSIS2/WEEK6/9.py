def isPrime(num):
    flag = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                flag = True
                break
    return flag

print(isPrime(int(input())))