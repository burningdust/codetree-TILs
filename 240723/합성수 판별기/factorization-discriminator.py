n = int(input())
yes = False

for i in range(2,n):
    if n%i==0:
        yes = True
        break

if yes:
    print("C")
else:
    print("N")