arr = list(map(int, input().split()))
num = arr[0] * arr[1] * arr[2]
sum_val = 0

def sum_digit(n):
    global sum_val
    if n == 0:
        return

    sum_val += n%10
    return sum_digit(n//10)

sum_digit(num)
print(sum_val)