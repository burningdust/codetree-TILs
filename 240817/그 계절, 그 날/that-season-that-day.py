def long_feb(Y):
    if Y%4==0:
        if Y%100==0:
            if Y%400==0:
                return True
            return False
        return True
    return False


def date_exist(Y,M,D):
    if M==2:
        if long_feb(Y) and D<=29:
            return True
        elif D<=28:
            return True
    elif M in [1,3,5,7,8,10,12] and D<=31:
        return True
    elif M in [4,6,9,11] and D<=30:
        return True
    else:
        return False


def season(M):
    if M==12 or M<=2:
        return "Winter"
    elif M<=5:
        return "Spring"
    elif M<=8:
        return "Summer"
    elif M<=11:
        return "Fall"


Y,M,D = tuple(map(int, input().split()))

print(season(M)) if date_exist(Y,M,D) else print(-1)