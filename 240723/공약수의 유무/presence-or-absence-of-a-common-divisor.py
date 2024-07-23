arr = input().split()
a,b = int(arr[0]), int(arr[1])

exist = False
for i in range(a,b+1):
    if 1920%i==0 and 2880%i==0:
        exist = True
        break

print(int(exist))