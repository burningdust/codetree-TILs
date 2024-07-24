n = int(input())
cnt = 1
for i in range(n*2):
    for _ in range(cnt):
        print("*", end=" ")
    print()

    if i+1>=n:
        cnt -= 1
    else:
        cnt += 1