def isPrime(num):
    if num <2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True


primes = [x for x in range(2,51) if isPrime(x)]
print(primes) 