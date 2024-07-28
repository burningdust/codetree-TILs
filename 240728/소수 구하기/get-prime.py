n = int(input())

for i in range(1,n+1):
    if i==1:
        continue
    elif i==2:
        print(i, end=" ")
        continue

    div_cnt = 0
    for j in range(2,i):
        if i%j==0:
            div_cnt += 1
    if div_cnt==0:
        print(i, end=" ")