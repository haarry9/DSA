def pair_sum_sorted_all_pairs(arr, start, target):
    l, r = start, len(arr)-1
    pairs = []
    while l<r:
        sum = arr[l] + arr[r]
        if sum == target:
            pairs.append([arr[l], arr[r]])
            l +=1
        # To avoid duplicate '[b,c]' pairs, skips 'b' if its the same as the previous number.
            while l<r and arr[l] == arr[l-1]:
                l+=1
        elif sum < target:
            l +=1
        else:
            r -=1
    return pairs


def triplet_sum(arr):

    arr.sort()
    triplets = []

    for i in range(len(arr)-2):
        # Optimization: triples consisting only of positive mumbers will nevr sum to 0
        if arr[i] > 0:
            break
        # To avoid duplicate triplets, skip `a` if its the same as the previous number
        if i > 0 and arr[i] == arr[i-1]:
            continue
        target = -arr[i]
        pairs = pair_sum_sorted_all_pairs(arr, i+1, target)
        for pair in pairs:
            triplets.append([arr[i]]+ pair)
    return triplets


arr = [-4, -4, -2, 0, 0, 1, 2, 3]
arr1 = [0,0,1,-1,1,-1]
print(triplet_sum(arr1))