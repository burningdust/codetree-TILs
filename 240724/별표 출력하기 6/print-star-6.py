n = int(input())
cnt = 0
for i in range(2*n-1):
    for _ in range(cnt):
        print(" ", end=" ")
    for _ in range(2*(n-cnt)-1):
        print("*", end=" ")
    print()
    
    if i<n-1:
        cnt += 1
    else:
        cnt -= 1