A = input()
B = input()
cnt = 0

for _ in range(len(A)):
    A = A[1:] + A[0]
    cnt += 1
    if A==B:
        break

print(cnt)