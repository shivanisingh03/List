# appending prime number in list



i=0
a=[]
while i<=100:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c+=1
        j+=1
    if c==2:
        a.append(i)
    i+=1
print(a)










