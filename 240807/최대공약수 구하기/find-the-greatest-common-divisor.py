def greatest_common_divisor(a,b):
    arr = []
    for i in range(1, max(a,b)):
        if a%i==0 and b%i==0:
            arr.append(i)
    print(arr[-1])


n,m = tuple(map(int, input().split()))
greatest_common_divisor(n,m)