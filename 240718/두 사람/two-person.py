A = input().split()
A_age, A_sex = int(A[0]), A[1]
B = input().split()
B_age, B_sex = int(B[0]), B[1]

print(int((A_age>=19 and A_sex=="M") or (B_age>=19 and B_sex=="M")))