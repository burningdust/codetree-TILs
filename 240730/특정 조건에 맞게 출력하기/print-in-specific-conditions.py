arr = list(map(int, input().split()))
arr_new = []
for i in arr:
    if i==0:
        break
    if i%2==0:
        arr_new.append(i//2)
    else:
        arr_new.append(i+3)

for i in arr_new:
    print(i, end=" ")