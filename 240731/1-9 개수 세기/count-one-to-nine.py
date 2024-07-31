n = int(input())
arr = list(map(int, input().split()))
arr_cnt = [0]*9

for elem in arr:
    arr_cnt[elem-1] += 1

for i in range(9):
    print(arr_cnt[i])