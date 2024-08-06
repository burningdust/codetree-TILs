A, B = input().split()
a, b = '', ''

for elem in A:
    if elem.isdigit():
        a += elem
    else:
        break
for elem in B:
    if elem.isdigit():
        b += elem
    else:
        break

print(int(a)+int(b))