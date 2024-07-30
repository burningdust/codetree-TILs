n = int(input())
arr = [1, n]
i = 1
while arr[i]<100:
    i += 1
    arr.append(arr[i-2] + arr[i-1])

for i in arr:
    print(i, end=" ")