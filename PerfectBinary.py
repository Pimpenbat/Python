def perfectBinaryNumbers(n):
    for i in range(n + 1):
        if isPerfect(i) is True:
            print(convBin(i))

def convBin(n):
    return bin(n).replace("0b", "")

def isPerfect(n):
    sum = 1 
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n / i
        i += 1
    return(True if sum == n and n != 1 else False)
