
number=[1,2,7,3,4,8,13,17,19,26,44,15,11,7,5,6,55]
i=0
a = []
b = []
while i<len(number):
    count=0
    k=2
    while k<number[i]:
        if number[i]%k==0:
            count+=1
        k+=1
    if count==0:
        print(number[i],"Prime")
        a.append(number[i])
    else:
        print(number[i],"Not Prime")
        b.append(number[i])
    i+=1
print(a)
print(b)



        
    
    
