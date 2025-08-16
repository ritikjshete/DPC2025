def MissingNum(a):
    n = len(a) + 1
    i, j = 1, 0
  
    while j < len(a) and i == a[j]:
        i += 1
        j += 1

    return i

print('no missing is ',MissingNum([1, 2, 3, 4]))
