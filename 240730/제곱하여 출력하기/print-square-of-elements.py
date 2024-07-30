n = int(input())
arr = list(map(int, input().split()))
arr_sqr = [i**2 for i in arr]
for i in arr_sqr:
    print(i, end=" ")