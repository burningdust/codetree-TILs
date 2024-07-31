arr = list(map(int, input().split()))
arr_cnt = [0]*9
for elem in arr:
    if elem==0:
        break
    elif elem//10==0:
        continue
    else:
        arr_cnt[elem//10-1] += 1

for i in range(9):
    print(i+1, "-", arr_cnt[i])