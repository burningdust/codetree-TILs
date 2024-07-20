arr = input().split()
a,b = int(arr[0]), int(arr[1])

for _ in range(a,b+1):
    if a<=b:
        print(a, end=" ")
        if a%2==1:
            a *= 2
        else :
            a += 3