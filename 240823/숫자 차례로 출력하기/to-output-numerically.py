def number_acs(n):
    if n == 0:
        return
    
    number_acs(n-1)
    print(n, end = " ")


def number_desc(n):
    if n == 0:
        return

    print(n, end = " ")
    number_desc(n-1)


N = int(input())
number_acs(N)
print()
number_desc(N)