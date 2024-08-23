def print_star(n):
    for i in range(n):
        print("*", end=" ")
    print()


def star_line(n):
    if n == 0:
        return
    print_star(n)
    star_line(n-1)
    print_star(n)
    

n = int(input())
star_line(n)