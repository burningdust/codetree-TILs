str_input = input()
str_obj = input()
satisfied = False

for i in range(len(str_input)-len(str_obj)+1):
    for j in range(len(str_obj)):
        if str_input[i+j]==str_obj[j]:
            satisfied = True
        else:
            satisfied = False
            break
    if satisfied:
        print(i)
        break

if not satisfied:
    print(-1)