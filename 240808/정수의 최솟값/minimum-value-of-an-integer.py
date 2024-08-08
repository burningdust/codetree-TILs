def min_val(a,b,c):
    min_val = a
    for i in (b,c):
        if i<min_val:
            min_val = i
    return min_val


a,b,c = tuple(map(int, input().split()))
print(min_val(a,b,c))