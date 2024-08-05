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

sum_val = 0
for elem in arr:
    sum_val += len(str(elem))
print(sum_val)

for elem in arr:
    print(elem, end="")