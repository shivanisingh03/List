


l=[1,2,3,[4,5,6]]
i=0
while i<len(l):
    if type(l[i])==list:
        j=0
        while j<len(l[i]):
            print(l[i][j])
            j+=1
    else:
        print(l[i])
    i+=1
