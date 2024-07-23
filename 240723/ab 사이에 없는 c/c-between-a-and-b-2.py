arr = input().split()
a,b,c = int(arr[0]), int(arr[1]), int(arr[2])
condition = True

for i in range(a,b+1):
    if i%c==0:
        condition = False
        break

if condition:
    print("YES")
else:
    print("NO")