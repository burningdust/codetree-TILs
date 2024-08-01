N = int(input())
arr = list(map(int, input().split()))
arr_2 = []

for i in range(N):
    cnt=0
    for j in range(N):
        if arr[i]==arr[j]:
            cnt += 1
    if cnt==1:
        arr_2.append(arr[i])

if arr_2:
    max_val = arr_2[0]
    for elem in arr_2:
        if max_val < elem:
            max_val = elem
    print(max_val)
else:
    print(-1)