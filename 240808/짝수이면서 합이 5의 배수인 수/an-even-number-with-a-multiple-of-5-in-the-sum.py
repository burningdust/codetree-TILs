def magic_num(n):
    arr = list(str(n))
    sum_val = 0
    for i in arr:
        sum_val += int(i)
    return n%2==0 and sum_val%5==0


n = int(input())
if magic_num(n):
    print("Yes")
else:
    print()