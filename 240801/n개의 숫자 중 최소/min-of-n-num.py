N = int(input())
arr = list(map(int, input().split()))
min_val = arr[0]
cnt = 0

for elem in arr[1:]:
    if min_val > elem:
        min_val = elem

for elem in arr:
    if min_val == elem:
        cnt += 1

print(min_val, cnt)