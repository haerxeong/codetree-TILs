def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: 
            return True
    return False
n = int(input())
print("C" if isPrime(n) else "N")