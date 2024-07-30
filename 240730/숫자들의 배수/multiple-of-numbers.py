n = int(input())
arr = [i*n for i in range(1,11)]
cnt=0
for i in arr:
    print(i, end=" ")
    if i%5==0:
        cnt+=1
    if cnt==2:
        break