arr = [input() for _ in range(10)]
letter = input()
none = True

for elem in arr:
    if elem[-1]==letter:
        print(elem)
        none = False

if none:
    print("None")