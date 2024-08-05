string = input()
n = int(input())
cnt = 0

for elem in string[::-1]:
    print(elem, end="")
    cnt += 1
    if cnt>=n:
        break