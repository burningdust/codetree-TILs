n = int(input())

for j in range(2):
    if j==0:
        a,b,c = 0,n,1
    else:
        a,b,c = n-1,-1,-1
    
    for i in range(a,b,c):
        if i%2==0:
            for _ in range(int(n-i/2)):
                print("*", end=" ")
            print()
        else:
            for _ in range(i//2+1):
                print("*", end=" ")
            print()