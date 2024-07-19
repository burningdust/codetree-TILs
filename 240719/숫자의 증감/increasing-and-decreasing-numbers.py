arr = input().split()
c,n = arr[0], int(arr[1])

if c=="A":
    for i in range(1,n+1):
        print(i, end=" ")
        i += 1
elif c=="D" :
    for _ in range(n):
        print(n, end=" ")
        n -= 1