# Q: How to find all pairs in an array of integers whose sum is equal to the given number?



number=30
n = [10, 11, 12, 13, 14, 17, 18, 19]
a=[]
i=0
while i<len(n):
    b=0
    while n[b]<n[i]:
        if number==n[b]+n[i]:
            a.append([n[i],n[b]])
        b = b+1
    i = i+1
print(a)






