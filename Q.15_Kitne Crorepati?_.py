# How many Crorepati?


kitna = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
i=0
sum=0
sam=0
count=0
while i<len(kitna):
    if kitna[i]<100000:
        count=count+1
    elif kitna[i]>100000 and kitna[i]<10000000:
        sum=sum+1
    else:
        sam=sam+1
    i=i+1
print("crorapati",sam)
print("lakhpati",sum)
print("diwale",count)



