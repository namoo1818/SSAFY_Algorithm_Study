# 5-5
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def facto(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(facto(5))