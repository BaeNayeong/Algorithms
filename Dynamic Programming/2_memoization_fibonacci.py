d = [0]*100

def fibonacci(n):
    if n == 1 or n ==2:
        return 1

    if d[n] == 0:
        d[n] = fibonacci(n-1)+fibonacci(n-2)

    return d[n]

print(fibonacci(99))