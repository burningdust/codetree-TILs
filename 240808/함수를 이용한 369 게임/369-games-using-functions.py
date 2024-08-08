def third_mul(n):
    return n%3==0


def _369(n):
    arr = list(map(int, str(n)))
    satisfied = False
    for i in arr:
        if i==3 or i==6 or i==9:
            satisfied = True
            break
    return satisfied


a,b = tuple(map(int, input().split()))
cnt = 0
for i in range(a,b+1):
    if third_mul(i) or _369(i):
        cnt += 1

print(cnt)