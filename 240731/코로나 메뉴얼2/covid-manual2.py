A = input().split()
B = input().split()
C = input().split()
arr_cnt = [0]*4

for sub in [A,B,C]:
    if int(sub[1])>=37:
        if sub[0]=="Y":
            arr_cnt[0] += 1
        else:
            arr_cnt[1] += 1
    else:
        if sub[0]=="Y":
            arr_cnt[2] += 1
        else:
            arr_cnt[3] += 1

for i in range(4):
    print(arr_cnt[i], end=" ")

if arr_cnt[0]>=2:
    print("E")