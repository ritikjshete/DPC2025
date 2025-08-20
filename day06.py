from collections import defaultdict

def findZeroSumSubarrays(arr):
    n = len(arr)
    prefix_sum = 0
    hashmap = defaultdict(list)
    result = []

    for i in range(n):
        prefix_sum += arr[i]

        if prefix_sum == 0:
            result.append((0, i))

        if prefix_sum in hashmap:
            for start in hashmap[prefix_sum]:
                result.append((start + 1, i))

        hashmap[prefix_sum].append(i)

    return result
