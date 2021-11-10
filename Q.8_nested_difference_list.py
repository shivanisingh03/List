
# Q: Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which numbers are not present in the second array.

list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7] 
num=[]
i=0
while i<len(list1):
    if list1[i] in list2:
        pass
    else:
        num.append(list1[i])
    i=i+1
print(num)








