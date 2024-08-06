s, q = tuple(input().split())
for _ in range(int(q)):
    quest = int(input())
    if quest == 1:
        s = s[1:] + s[0]
    elif quest == 2:
        s = s[-1] + s[:-1]
    else:
        s = s[::-1]
    print(s)