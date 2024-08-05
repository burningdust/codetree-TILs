arr = ["apple", "banana", "grape", "blueberry", "orange"]
given = input()
cnt = 0
for string in arr:
    for letter in string[2:4]:
        if letter == given:
            print(string)
            cnt+=1
            break
print(cnt)