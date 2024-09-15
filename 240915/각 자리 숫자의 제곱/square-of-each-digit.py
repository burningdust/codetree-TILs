def digit_sqr(n):
    if n//10 == 0:
        return n**2
    return digit_sqr(n//10) + (n%10)**2


N = int(input())
print(digit_sqr(N))