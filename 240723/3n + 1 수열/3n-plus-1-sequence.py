N = int(input())
cnt = 0
while True:
    if N==1:
        print(cnt)
        break
    if N%2==0:
        N = int(N/2)
    elif N%2==1:
        N = N*3+1
    cnt += 1