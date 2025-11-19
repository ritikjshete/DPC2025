import math
 
def merge(arr1, arr2, m, n):
    def nextGap(gap):
        if gap <= 1:
            return 0
        return math.ceil(gap / 2)

    gap = nextGap(m + n)
    while gap > 0:
        i = 0
        j = gap

        while j < (m + n):
            if i < m and j < m:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]

            elif i < m and j >= m:
                if arr1[i] > arr2[j - m]:
                    arr1[i], arr2[j - m] = arr2[j - m], arr1[i]

            else:
                if arr2[i - m] > arr2[j - m]:
                    arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]

            i += 1
            j += 1

        gap = nextGap(gap)


