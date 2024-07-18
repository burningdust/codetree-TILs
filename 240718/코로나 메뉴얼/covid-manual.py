A = input().split()
A_sym, A_tem = A[0], int(A[1])
B = input().split()
B_sym, B_tem = B[0], int(B[1])
C = input().split()
C_sym, C_tem = C[0], int(C[1])

A_cor = 1 if (A_sym=="Y" and A_tem>=37) else 0
B_cor = 1 if (B_sym=="Y" and B_tem>=37) else 0
C_cor = 1 if (C_sym=="Y" and C_tem>=37) else 0

if (A_cor+B_cor+C_cor)>=2 :
    print("E")
else :
    print("N")