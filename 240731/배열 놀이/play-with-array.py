num = input().split()
n,q = int(num[0]), int(num[1])
arr = list(map(int,input().split()))

for _ in range(q):
    Q = list(map(int, input().split()))

    if Q[0]==1:
        print(arr[Q[1]-1])

    elif Q[0]==2:
        if Q[1] in arr:
            print(arr.index(Q[1])+1)
        else:
            print(0)
    
    else:
        for i in range(Q[1]-1, Q[2]):
            print(arr[i], end=" ")
        print()