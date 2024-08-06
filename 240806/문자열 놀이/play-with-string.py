s,q = tuple(input().split())
arr = list(s)

for _ in range(int(q)):
    question = list(input().split())
    if question[0] == "1":
        a, b = int(question[1]), int(question[2])
        arr[a-1], arr[b-1] = arr[b-1], arr[a-1]
        print(''.join(arr))
    else:
        for i in range(len(arr)):
            if arr[i] == question[1]:
                arr[i] = question[2]
        print(''.join(arr))