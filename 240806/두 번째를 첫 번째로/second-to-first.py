arr = list(input())
letter = arr[1]
for i in range(1,len(arr)):
    if arr[i]==letter:
        arr[i] = arr[0]
print(''.join(arr))