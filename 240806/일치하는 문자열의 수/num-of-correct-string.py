n, A = tuple(input().split())
cnt = 0
for _ in range(int(n)):
    word = input()
    if word == A:
        cnt += 1
print(cnt)