
# Ek list mein appke paas marks hain. Inn marks ka sum kar ke total marks nikalne ka code likha hua hai,
# lekin yeh code chalta nahi hai. Sahi kar ke submit karo.


marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
total_marks = 0
counter = 0
while counter < len(marks):
    total_marks = total_marks + int(marks[counter])
    counter = counter + 1 
print(total_marks)
