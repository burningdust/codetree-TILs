score = input().split()
mid_score, fin_score = int(score[0]), int(score[1])

if mid_score<90 :
    print(0)
elif fin_score>=95:
    print(100000)
elif fin_score>=90:
    print(50000)
else:
    print(0)