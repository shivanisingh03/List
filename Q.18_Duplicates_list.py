# iss lists mei se duplicates nikal kar, kisi aur list mei daal kar print karne hai.

n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
new=[]
i=0
while i<len(n):
    j=0
    count=0
    while j<len(n):
        if n[i]==n[j]:
            count=count+1
            if count==2:
                if n[i] not in new:
                    new.append(n[i])
        j+=1
    i=i+1
print(new)













