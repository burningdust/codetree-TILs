n = int(input())

for i in range(n):
    for j in range(n):
        if i==0 or (j%2!=0 and i<j+1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()