string, letter = tuple(input().split())
if letter in string:
    print(string.index(letter))
else:
    print("No")