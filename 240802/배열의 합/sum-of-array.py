arr = [list(map(int, input().split())) for _ in range(4)]
for row in arr:
    sum_val = 0
    for elem in row:
        sum_val += elem
    print(sum_val)