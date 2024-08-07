def lowest_common_multiple(a,b):
    mul_a = [a*i for i in range(1,b+1)]
    mul_b = [b*i for i in range(1,a+1)]
    result = 1
    for elem_a in mul_a:
        for elem_b in mul_b:
            if elem_a == elem_b:
                result = elem_a
                break
        if result == elem_a:
            break
    print(result)


n,m = tuple(map(int, input().split()))
lowest_common_multiple(n,m)