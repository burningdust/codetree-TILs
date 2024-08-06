A = input()
B = input()
cnt = 0
for i in range(len(A)-1):
    satisfied = False
    for j in range(2):
        if A[i+j]==B[j]:
            satisfied = True
        else:
            satisfied = False
            break
    if satisfied:
        cnt += 1
print(cnt)