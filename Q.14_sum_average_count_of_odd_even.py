# Ek code likho jo kisi bhi list ke liye yeh output karta hai, ki uss list mei odd numbers, even numbers 
# aur sab numbers ka: - count

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
sum=0
even=0
sum1=0
odd=0
while i<len(elements):
    if elements[i]%2==0:
        sum=sum+elements[i]
        even+=1
    else:
        sum1=sum1+(elements[i])
        odd+=1
    i=i+1
print(sum//even)  
print(sum1//odd)    


