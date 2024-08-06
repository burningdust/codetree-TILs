A = input()
B = input()
cnt = 0
satisfied = True

while A!=B:
    A = A[1:] + A[0]
    cnt += 1
    if cnt>=len(A):
        print(-1)
        satisfied = False
        break

if satisfied:
    print(cnt)