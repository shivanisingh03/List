# Code likho jo di gayi list mein jo number 20 se bade hai aur 40 se chote hai unhe count kare. Aur firr unka count print kare.



# Maan lo humare paas ek list of marks hain aur humne yeh nikalna hai ki kitne bachon ke marks 50 se kam hai aur kitno ke zyada. Yeh karne ke liye hum yeh 
# code likhenge.


# student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# list_length = len(student_marks)
# index = 0
# less_than50 = 0
# more_than50 = 0
# while index < list_length:
#     marks = student_marks[index]
#     if marks < 50:
#         less_than50 = less_than50 + 1
#     else:
#         more_than50 = more_than50 + 1
#     index = index + 1
# print ("Marks more than 50: " + str(more_than50),student_marks)
# print ("Marks less than 50: " + str(less_than50),student_marks) 



# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
# i=0
# less_then=0
# more_then=0
# while i<numbers:
#     marks=numbers(i)
#     if marks<20:
#         less_then20=less_then20+1
#     else:
#         more_than40=more_than40+1
#     i=i+1
# print ("Marks more than 20: " + str(more_than50),numbers)
# print ("Marks less than 40: " + str(less_than50),numbers)




# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
# list_length = len(numbers)
# index = 0
# less_than20 = 0
# more_than40 = 0
# while index < list_length:
#     marks = numbers[index]
#     if marks < 20:
#         less_than20 = less_than20 + 1
#     if marks <40:
#         more_than40= more_than40 + 1
#     index = index + 1
# print ("Marks more than 20: " + str(more_than20),numbers)
# print ("Marks less than 40: " + str(less_than40),numbers)


# Code likho jo di gayi list mein jo number 20 se bade hai aur 40 se chote hai unhe count kare. Aur firr unka count print kare.


# Write a code, that counts the numbers between 20 and 40 and then print its count.


numbers=[50, 40, 23, 70,25, 56,12, 5, 10, 7] 
count=0
i=0
length=len(numbers)
while i<length:
    a=numbers[i]
    if a>20 and a<40:
        print(a)
        count+=1
    i=i+1
print(count)





