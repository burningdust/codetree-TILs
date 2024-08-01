arr = input().split()
n1,n2 = int(arr[0]), int(arr[1])
A = input().split()
B = input().split()
satisfied = False

for i in range(n1-n2+1):
    A_sub = []
    for j in range(n2):
        A_sub.append(A[i+j])
    if A_sub == B:
        satisfied = True
        break

print("Yes") if satisfied else print("No")