n = int(input())
for i in range(n):
    cnt = n-i
    for j in range(n):
        if i>=j:
            print(cnt, end=" ")
            cnt += 1
        else:
            print(" ", end=" ")
    print()