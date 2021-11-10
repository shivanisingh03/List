# Ek code likho jo kissi bhi list ke liye uss list ke do sum ka output karta hai, ki uss list mei odd 
# numbers ka sum aur even numbers ka sum kitna hai.


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
even=0
odd=0
while i<len(elements):
    if elements[i]%2==0:
        even=even+(elements[i])
    else:
        odd=odd+(elements[i])
    i=i+1
print("even",even)
print("odd",odd)











