num = 0

def divide(n):
    global num

    if n == 1:
        return num

    num += 1
    if n%2 == 0:
        return divide(n//2)
    else:
        return divide(n//3)


N = int(input())
print(divide(N))