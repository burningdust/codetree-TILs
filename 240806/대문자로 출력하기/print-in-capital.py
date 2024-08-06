str1 = input()
for elem in str1:
    if elem.isalpha():
        if elem>='a' and elem<='z':
            print(chr(ord(elem) - ord('a') + ord('A')), end="")
        else:
            print(elem, end="")