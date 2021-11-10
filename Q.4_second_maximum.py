# Code likho jo iss list mein se second maximum element (doosra sabse bada element) dhund kar kar print kare.

numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
i=0
s=numbers[i]
while i<len(numbers):
    m=numbers[i]
    if m>s:
        s=m
    i=i+1
numbers.remove(s)
k=0
j=numbers[1]
while k<len(numbers):
    a=numbers[k]
    if a>j:
        j=a
    k=k+1
print(j)