n,m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))


def sum_range():
    global m, arr
    for _ in range(m):
        sum_val = 0
        a1, a2 = tuple(map(int, input().split()))
        for i in range(a1-1, a2):
            sum_val += arr[i]
        print(sum_val)

sum_range()