str1 = input()
arr = list(str1)

for i in range(len(arr)):
    if arr[i]==str1[0]:
        arr[i] = str1[1]
    elif arr[i]==str1[1]:
        arr[i] = str1[0]

print(''.join(arr))