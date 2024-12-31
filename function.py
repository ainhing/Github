def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
def A(n,k):
    return factorial(n)//factorial(n-k)
def C(n,k):
    return factorial(n)//(factorial(k)*factorial(n-k))