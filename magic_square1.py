

magic_square=  [
    [5, 3, 7],
    [1, 8, 9],
    [6, 4, 2]
] 
index=0
option=0
while index<len(magic_square):
    count=0
    while count<len(magic_square):
        point=magic_square[count][index]
        option=option+point
        count=count+1
    index+=1
print(option//len(magic_square))