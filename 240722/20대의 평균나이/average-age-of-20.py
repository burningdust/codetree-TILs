sum_val = 0
cnt = 0

while True:
    n = int(input())
    if n>=20 and n<30:
        sum_val += n
        cnt += 1
    else:
        print(f"{sum_val/cnt:.2f}")
        break