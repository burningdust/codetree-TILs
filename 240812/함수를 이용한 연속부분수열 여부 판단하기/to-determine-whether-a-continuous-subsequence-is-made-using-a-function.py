def subsequence(n1, n2, A, B):
    for i in range(0, n1-n2+1):
        if A[i:i+n2]==B:
            return True
    return False


n1,n2 = tuple(map(int, input().split()))
A = input().split()
B = input().split()

if subsequence(n1, n2, A, B):
    print("Yes")
else:
    print("No")