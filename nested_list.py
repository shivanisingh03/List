

a=[2,4,6]
b=[8,2,5]
c=[]
i=0
while i<len(a):
    j=0
    while j<len(b):
        d=a[i]+b[i]
        c.append(d)
        j+=1
        i+=1
    print(c)
    
