arr = list(map(int, input().split()))
arr_result = []
for i in arr:
    if i==0:
        break
    arr_result.append(i)

for i in arr_result[::-1]:
    print(i, end=" ")