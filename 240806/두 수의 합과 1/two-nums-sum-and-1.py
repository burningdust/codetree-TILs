a,b = tuple(map(int, input().split()))
sum_val = a+b
cnt = 0
for elem in str(sum_val):
    if elem=='1':
        cnt += 1
print(cnt)