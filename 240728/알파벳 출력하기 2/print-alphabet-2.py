n = int(input())
cnt = ord("A")

for i in range(n):
    for j in range(n):
        if i<=j:
            print(chr(cnt), end=" ")
            if chr(cnt)=="Z":
                cnt = ord("A")
            else:
                cnt += 1
        else:
            print(" ", end=" ")
    print()