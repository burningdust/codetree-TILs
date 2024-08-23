def flower(n):
    if n == 0:
        return
    
    print(n, end = " ")
    flower(n-1)
    print(n, end = " ")


N = int(input())
flower(N)