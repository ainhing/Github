def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact*=i
    return fact
def combination(n,k):
    return factorial(n) // (factorial(n - k) * factorial(k))
