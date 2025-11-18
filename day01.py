def sortlist(a):
    if len(a) == 0:
        return []
     
    zero, one, two = [], [], []
    for i in a: 
        if i == 0:
            zero.append(i)
        elif i == 1:
            one.append(i)
        else:
            two.append(i)

    return zero + one + two

print(sortlist([0, 1, 2, 1, 0, 2, 1, 0])) 
