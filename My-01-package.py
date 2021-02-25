import numpy as np
original_price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 33]

for i in range(item):
    line=i+1
    val = original_price[i]
    for j in range(maxP+1):
        s[line,j]=s[line-1,j] if j < val else max(s[line-1,j],s[line-1,j-val]+val)

        '''
        if(j<val):
            s[line,j]=s[line-1,j]
        else:
            s[line,j]=max(s[line-1,j], s[line-1,j-val]+val)
        '''
def getpath(n):
    if(n>maxP):
        print("No path")
        return
    pt=[]
    m=n
    for i in range(item,0,-1):
        #print(i,' ',m)
        if s[i,m]== s[i-1,m-original_price[i-1]]+original_price[i-1]:
            pt.append(original_price[i-1])
            m -=original_price[i-1]
    pt.reverse()
    return pt

a=getpath(26)
print(a)