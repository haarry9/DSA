def triplet_sum_brute_force1(arr):
    triplet_arr = []
    for i in range(0, len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if (arr[i] + arr[j] + arr[k] == 0):
                    triplet_arr.append([arr[i], arr[j], arr[k]])
    
    return triplet_arr

def triplet_sum_brute_force2(arr):
    # using hashmaps to ensure we don't add duplicate triplets
    triplets = set()
    for i in range(0, len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if (arr[i] + arr[j] + arr[k] == 0):
                    # sort the triplet before adding it in the hash set
                    triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
                    triplets.add(triplet)
    
    return [list(triplet) for triplet in triplets]

arr = [0, -1, 2, -3, 1]
print(triplet_sum_brute_force2(arr))
print(triplet_sum_brute_force1(arr))