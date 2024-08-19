def distinct(A):
    for i in range(len(A)-1):
        if A[i]!=A[i+1]:
            return True
    return False


A = input()
print("Yes") if distinct(A) else print("No")