N = int(input())

def sum_odd_even(n):
    if n<=2:
        return n
    return n + sum_odd_even(n-2)


print(sum_odd_even(N))