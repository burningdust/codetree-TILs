n = int(input())
cnt = 1
for i in range(n):
    if i%2==0:
        for _ in range(n):
            print(cnt, end=" ")
            cnt += 1
    else:
        cnt += n-1
        for _ in range(n):
            print(cnt, end=" ")
            cnt -= 1
        cnt += n+1
    print()