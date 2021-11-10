
# diffrence between the numbers 

a=[1,3,5,7,9,10,15,1]
i=0
b=[]
while i<len(a)-1:
    c=a[i+1]
    c=c-a[i]
    b.append(c)
    i+=1
print(b)
