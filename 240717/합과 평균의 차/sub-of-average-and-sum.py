arr = input().split()
a,b,c = int(arr[0]), int(arr[1]), int(arr[2])
sum_arr = a+b+c
mean_arr = sum_arr/len(arr)
print(sum_arr, mean_arr, sum_arr - mean_arr, sep="\n")