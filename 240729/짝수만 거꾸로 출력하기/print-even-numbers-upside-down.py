n = int(input())
arr = list(map(int, input().split()))
arr_even = []
for i in arr:
    if i%2==0:
        arr_even.append(i)
for i in arr_even[::-1]:
    print(i, end=" ")