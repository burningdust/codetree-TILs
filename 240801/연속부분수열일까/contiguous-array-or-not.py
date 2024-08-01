arr = input().split()
n1,n2 = int(arr[0]), int(arr[1])
A = input().split()
B = input().split()

for i in range(n1-n2):
    satisfied = False
    if A[i] == B[0]:     
        for j in range(n2):
            if A[i+j] == B[j]:
                satisfied = True
            else:
                satisfied = False
                break
    if satisfied:
        break
            
print ("Yes") if satisfied else print("No")