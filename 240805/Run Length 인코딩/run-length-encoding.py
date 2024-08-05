A = input()
cnt = 1
arr = [A[0]]

for i in range(1, len(A)):
    if A[i]==A[i-1]:
        cnt += 1
    else:
        arr.append(cnt)
        arr.append(A[i])
        cnt = 1

arr.append(cnt)
        
print(len(arr))
for elem in arr:
    print(elem, end="")