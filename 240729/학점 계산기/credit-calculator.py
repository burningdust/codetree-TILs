n = int(input())
score = list(map(float, input().split()))
print(f"{sum(score)/n:.1f}")
if sum(score)/n >= 4.0:
    print("Perfect")
elif sum(score)/n >= 3.0:
    print("Good")
else:
    print("Poor")