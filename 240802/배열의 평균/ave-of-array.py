arr = [list(map(int, input().split())) for _ in range(2)]

for i in range(2):
    sum_row = 0
    for j in range(4):
        sum_row += arr[i][j]
    print(f"{sum_row/4:.1f}", end=" ")

print()

for j in range(4):
    sum_col = 0
    for i in range(2):
        sum_col += arr[i][j]
    print(f"{sum_col/2:.1f}", end=" ")

print()

sum_val = 0
for i in range(2):
    for j in range(4):
        sum_val += arr[i][j]
print(f"{sum_val/8:.1f}")