arr = input().split()
sum_val, cnt = 0, 0

for elem in arr:
    n = int(elem)
    if n>=250:
        break
    sum_val += n
    cnt += 1

print(sum_val, f"{sum_val/cnt:.1f}")