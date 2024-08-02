arr = [input().split() for _ in range(5)]

ord("A") - ord("a")
for i in range(5):
    for j in range(3):
        print(chr(ord(arr[i][j]) + ord("A") - ord("a")), end=" ")
    print()