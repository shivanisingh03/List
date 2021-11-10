# which number skip between the numbers

a=[1,3,5,7,9,10,15,1]
b=[]
i=1
# l=len(a)
c=0
while i<=15:
    c+=1
    if i not in a:
        b.append(i)
    i+=1
print(b)

