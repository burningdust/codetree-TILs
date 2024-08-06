arr = []
while True:
    word = input()
    if word=='0':
        break
    arr.append(word)
print(len(arr))
for elem in arr[::2]:
    print(elem)