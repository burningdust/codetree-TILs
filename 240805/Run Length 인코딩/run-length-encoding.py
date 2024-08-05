A = input()
cnt = 1
arr = []

arr.append(A[0])
for i in range(1, len(A)-1):
    if A[i]==A[i-1]:
        cnt += 1
    else:
        arr.append(cnt)
        arr.append(A[i])
        cnt = 1

if A[-2]!=A[-1]:
    arr.append(A[-1])
    cnt = 1
else:
    cnt += 1
arr.append(cnt)

print(len(arr))
for elem in arr:
    print(elem, end="")