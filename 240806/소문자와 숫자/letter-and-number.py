str1 = input()
for elem in str1:
    if elem.isdigit():
        print(elem, end="")
    elif elem.isalpha():
        if elem>="A" and elem<="Z":
            print(chr(ord(elem) - ord("A") + ord("a")), end="")
        else:
            print(elem, end="")