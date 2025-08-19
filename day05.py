def leader(a):
    n = len(a)
    led = []
    
    for i in range(n):
        temp = True
        for j in range(i + 1, n):
            if a[j] > a[i]:
                temp = False
                break
        if temp:
            led.append(a[i])
    
    return led
    
print(leader([100, 50, 20, 10]))
