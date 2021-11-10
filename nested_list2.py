a=[2,4,[9,4,7,[5,4,3],6,7,8]]
i=0
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                c=0
                while c<len(a[i][j]):
                    # print(i,j,c,a[i][j][c])
                    sum+=(a[i][j][c])
                    c+=1
            else:
                # print(j,a[i][j])
                sum+=(a[i][j])
            j+=1
    else:
        # print(i,a[i])
        sum+=(a[i])
    i+=1
print(sum)