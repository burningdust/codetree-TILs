A = input().split()
A_math, A_eng = int(A[0]), int(A[1])

B = input().split()
B_math, B_eng = int(B[0]), int(B[1])

print(int(A_math>B_math and A_eng>B_eng))