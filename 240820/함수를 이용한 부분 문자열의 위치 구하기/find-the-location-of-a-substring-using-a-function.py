input_str = input()
obj_str = input()
n1 = len(input_str)
n2 = len(obj_str)

def sub_string():
    for i in range(n1-n2+1):
        if input_str[i:i+n2] == obj_str:
            return i
    return -1


print(sub_string())