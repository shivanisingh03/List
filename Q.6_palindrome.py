# Palindrome wo strings ya numbers hote hai jo ulta seedhe same hote hai. Jaise, NITIN. Nitin ko aap left se padho ya right se, nitin hi hai. Aise hi MOM bhi 
# ek palindrome hai. Code likho jo check kare ki kya list palindrome hai ya nahi. Aur print karo “Haan! palindrome hai” agar hai. Aur “nahi! Palindrome nahi 
# hai” agar nahi hai. Abhi ke liye iss list ko use kar ke code likh sakte ho:


string=[ 'n', 'i', 't', 'i', 'n' ]
reverse=[]
index=len(string)
while index>0:
    reverse.append(string[index-1])
    index=index-1
if reverse==string:
    print("it is palindrom ")
else:
    print("not ")



