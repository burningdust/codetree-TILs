n = int(input())
sum_val = 0
for _ in range(n):
    sum_val += int(input())
print(str(sum_val)[1:]+str(sum_val)[0])