def sum_even(n):
    sum_val = 0
    arr = list(str(n))
    for i in arr:
        sum_val += int(i)
    if sum_val%2==0:
        return True
    else:
        return False


def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True


a,b = tuple(map(int, input().split()))
cnt = 0
for i in range(a,b+1):
    if sum_even(i) and prime(i):
        cnt += 1

print(cnt)