arr = input().split()
sum_arr = sum(arr)
mean_arr = int(sum_arr/len(arr))
print(sum_arr, mean_arr, sum_arr-mean_arr, sep="\n")