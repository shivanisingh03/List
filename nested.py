
# sum of nested list in while loop

a=[1,2,[3,4,5,[1,2,3,[4,5,6]]],6,[7,8],[9,10]]
i=0
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                c=0
                while c<len(a[i][j]):
                    if type(a[i][j][c])==list:
                        k=0
                        while k<len(a[i][j][c]):
                            sum=sum+a[i][j][c][k]
                            k+=1
                    else:
                        sum=sum+a[i][j][c]
                    # sum+=a[i][j][c]
                    c+=1
            else:
                sum+=a[i][j]
            j+=1
    else:
        sum=sum+a[i]
    i+=1
print(sum)



# sum of nested list in for loop

            
a=[1,2,[3,4,5,[1,2,3,[4,5,6]]],6,[7,8],[9,10]]
i=0
sum=0
for i in a:
    if type(i)==list:
        for j in i:
            if type(j)==list:
                for c in j:
                    if type(c)==list:
                        for k in c:
                            sum=sum+k
                    else:
                        sum=sum+c
            else:
                sum+=j
    else:
        sum=sum+i
print(sum)















              













