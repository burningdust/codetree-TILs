A = input()
B = input()
a, b = '',''

for elem in A:
    if elem.isdigit():
        a += elem

for elem in B:
    if elem.isdigit():
        b += elem

print(int(a)+int(b))