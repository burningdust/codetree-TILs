n,m = tuple(map(int, input().split()))
A = list(map(int, input().split()))


def calculate():
    global m
    sum_val = 0
    while True:
        sum_val += A[m-1]
        if m==1:
            return sum_val
        elif m%2==1:
            m -= 1
        else:
            m = int(m/2)
        
        
    

print(calculate())