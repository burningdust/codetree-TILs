n = int(input())

for i in range(n):
    if i%2==0:
        for _ in range(int(i/2+1)):
            print("*", end=" ")
        print()
    else:
        for _ in range(int(n-i/2+1)):
            print("*", end=" ")
        print()

for i in range(n-1,-1,-1):
    if i%2==0:
        for _ in range(int(i/2+1)):
            print("*", end=" ")
        print()
    else:
        for _ in range(int(n-i/2+1)):
            print("*", end=" ")
        print()