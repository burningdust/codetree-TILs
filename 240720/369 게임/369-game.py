n = int(input())

for i in range(1,n+1):
    tenth = i//10
    oneth = i%10
    if i%3==0 or (tenth!=0 and tenth%3==0) or (oneth!=0 and oneth%3==0):
        print(0, end=" ")
    else :
        print(i, end=" ")