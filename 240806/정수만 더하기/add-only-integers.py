A = input()
sum_val = 0
for elem in A:
    if elem.isdigit():
        sum_val += int(elem)

print(sum_val)