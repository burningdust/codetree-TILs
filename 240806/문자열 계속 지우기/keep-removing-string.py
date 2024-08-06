A = input()
B = input()
while B in A:
    idx = A.index(B)
    arr = list(A)
    for _ in range(len(B)):
        arr.pop(idx)
    A = ''.join(arr)
print(A)