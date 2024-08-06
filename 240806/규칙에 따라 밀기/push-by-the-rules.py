A = input()
command = input()
for elem in command:
    if elem == "L":
        A = A[1:] + A[0]
    else:
        A = A[-1] + A[:-1]
print(A)