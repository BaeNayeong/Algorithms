d = [0]*100

def fibonacci(n):

    d[1]=1
    d[2]=1

    for i in range(3, n+1):
        d[i]=d[i-1]+d[i-2]

    return d[n]

print(fibonacci(6))