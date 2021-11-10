list=[[1,2,3,4],[5,6,7,8],[9,10,11,14]]
i=0
count_even=0
count_odd=0
sum_even=0
sum_odd=0
while i<len(list):
    j=0
    while j<len(list[i]):
        if list[i][j]%2==0:
            sum_even=sum_even+(list[i][j])
            count_even+=1
        else:
            sum_odd=sum_odd+(list[i][j])
            count_odd+=1
        j+=1
    i+=1
print("even",sum_even,count_even)
print("odd",sum_odd,count_odd)


