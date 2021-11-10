# Humei char_list mei jo bhi characters hai, unki occurences count karni hai, aur ek nested list mei 
# save karni hai, phir uss nested list ko use kar kar jo output hai, woh print karna hai.

# n=[50,40,23,70,56,12]
# i=0
# count=0
# while i<len(n):
#     count+=1
#     i+=1
# print(count)



# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# i=0
# new=[]
# while i<len(char_list):
#     j=0
#     count=0
#     while j<len(char_list):
#         if char_list[i]==char_list[j]:
#             count = count+1
#         j+=1
#     new.append(count)
#     new.append(char_list[i])
#     i=i+1
# print(new)



char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# char_list =[1,1,2,2,4,4,5,5,5]
i=0
new=[]
while i<len(char_list):
    j=0
    count=0
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count = count+1
        j+=1
    if char_list[i]in new:
        i+=1
        continue
    new.append(char_list[i])
    print(char_list[i],"are",count)
print(new)                                                                                                                                                                                                                             









