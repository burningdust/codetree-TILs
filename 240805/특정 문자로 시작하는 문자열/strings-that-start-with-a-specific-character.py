n = int(input())
arr = [input() for _ in range(n)]
letter = input()
sum_val, cnt = 0, 0

for elem in arr:
    if elem[0]==letter:
        cnt += 1
        sum_val += len(elem)

print(cnt, f"{sum_val/cnt:.2f}")