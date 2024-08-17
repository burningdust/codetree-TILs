def date_exist(M,D):
    if M==2 and D<=28:
        return True
    elif M in [1,3,5,7,8,10,12] and D<=31:
        return True
    elif M in [4,6,9,11] and D<=30:
        return True
    else:
        return False


M,D = tuple(map(int, input().split()))

print("Yes") if date_exist(M,D) else print("No")