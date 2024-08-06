A = input()
B = input()
cnt = 0

while A!=B:
    A = A[1:] + A[0]
    cnt += 1

print(cnt)