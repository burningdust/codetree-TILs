n = int(input())
sum_val = 0
cnt = 0

for _ in range(n):
    num = int(input())
    sum_val += num
    cnt += 1

print(sum_val, f"{sum_val/cnt:.1f}")