arr = input().split()
a,b = int(arr[0]), int(arr[1])
arr_rem = [0]*b

while a>1:
    arr_rem[a%b] += 1
    a //= b

sum_val = 0
for i in range(b):
    sum_val += arr_rem[i]**2

print(sum_val)