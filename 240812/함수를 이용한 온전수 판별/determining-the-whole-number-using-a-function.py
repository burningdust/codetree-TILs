def magic_num(n):
    if n%2==0 or n%10==5:
        return False
    elif n%3==0 and n%9!=0:
        return False
    else:
        return True
    

a,b = tuple(map(int, input().split()))
cnt = 0
for i in range(a,b+1):
    if magic_num(i):
        cnt += 1

print(cnt)