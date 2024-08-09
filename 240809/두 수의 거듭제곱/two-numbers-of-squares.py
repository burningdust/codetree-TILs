def square(a,b):
    return a**b


a,b = tuple(map(int, input().split()))
print(square(a,b))