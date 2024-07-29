arr = list(map(int, input().split()))
sum_val, cnt = 0, 0

for i in arr:
    if i==0:
        break
    sum_val += i
    cnt += 1

print(sum_val, f"{sum_val/cnt:.1f}")