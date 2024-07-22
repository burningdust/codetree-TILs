while True:
    arr = input().split()
    width = int(arr[0])
    length = int(arr[1])
    letter = arr[2]
    print(width*length)
    if letter=="C":
        break