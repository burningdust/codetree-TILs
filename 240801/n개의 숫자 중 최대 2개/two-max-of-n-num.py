N = int(input())
arr = list(map(int, input().split()))

first = arr[0]
for n in arr:
    if first < n:
        first = n

arr.remove(first)
second = arr[0]
for n in arr:
    if second < n:
        second = n 

print(first, second)