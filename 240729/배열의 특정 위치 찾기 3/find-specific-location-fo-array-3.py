arr = list(map(int, input().split()))
arr_result = []
for i in arr:
    if i==0:
        break
    arr_result.append(i)
print(arr_result[-1]+arr_result[-2]+arr_result[-3])