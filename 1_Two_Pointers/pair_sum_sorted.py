def pair_sum_sorted_brute_force(arr, target):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j] == target):
                return [i, j]
    
    return []

# Optimial solution using two pointers
def pair_sum_sorted(arr, target):
    l = 0
    r = len(arr)-1
    while (l<r):
        sum = arr[l] + arr[r]
        if (sum < target):
            l +=1
        elif (sum > target):
            r -= 1
        else:
            return [l,r]
    
    return []




arr = [-3,-2,-1]
# print(pair_sum_sorted_brute_force(arr,7))
print(pair_sum_sorted(arr,-5))