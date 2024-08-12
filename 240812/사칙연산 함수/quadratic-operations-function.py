def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return int(a/b)


cal = input().split()
a,o,c = int(cal[0]), cal[1], int(cal[2])

if o=='+':
    result = add(a,c)
elif o=='-':
    result = sub(a,c)
elif o=='*':
    result = mul(a,c)
elif o=='/':
    result = div(a,c)
else:
    result = False

print(a,o,c,'=',result)