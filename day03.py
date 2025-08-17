def dubNum(a):
    out=0
    for i in a:
        count=0
        for j in a:
           if i==j:
               count+=1
               out=i

        if count>=2:
            break
        
    return out
  
print('no Dublicate is ',dubNum( [1, 4, 4, 2, 3]))
