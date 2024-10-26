N = int(input())
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
x, y = 0, 0

for _ in range(N):
    move = input().split()

    if move[0] == "E":
        dir_num = 0
    elif move[0] == "N":
        dir_num = 1
    elif move[0] == "W":
        dir_num = 2
    else:
        dir_num = 3

    for _ in range(int(move[1])):
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)