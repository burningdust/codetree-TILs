arr = list(map(int, input().split()))
arr_small = []
arr_big = []

for n in arr:
    if n<500:
        arr_small.append(n)
    elif n>500:
        arr_big.append(n)

max_val = arr_small[0]
min_val = arr_big[0]

for n in arr_small:
    if max_val < n:
        max_val = n

for n in arr_big:
    if min_val > n:
        min_val = n

print(max_val, min_val)