n = int(input())
arr = input().split()
result = "".join(arr)
cnt = 0
for elem in result:
    print(elem, end="")
    cnt += 1
    if cnt%5==0:
        print()