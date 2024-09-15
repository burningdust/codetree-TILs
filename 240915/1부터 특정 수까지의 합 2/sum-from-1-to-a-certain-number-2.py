def sum_all(n):
    if n == 1:
        return 1
    return sum_all(n-1) + n


N = int(input())
print(sum_all(N))