arr = input().split()
a,b = int(arr[0]), int(arr[1])

rate = a/b
print(int(rate), end=".")

for _ in range(20):
    rate -= int(rate)
    rate*=10
    print(int(rate), end="")