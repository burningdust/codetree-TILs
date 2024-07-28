n = int(input())
cnt = ord("A")
for i in range(n):
    for _ in range(i+1):
        print(chr(cnt), end="")
        if chr(cnt)=="Z":
            cnt = ord("A")
        else:
            cnt +=1
    print()