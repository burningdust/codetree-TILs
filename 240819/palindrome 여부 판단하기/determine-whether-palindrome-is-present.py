def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


A = input()
print("Yes") if palindrome(A) else print("No")