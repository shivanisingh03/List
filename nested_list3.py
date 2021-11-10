a=[1,2,[3,4,5,],6,7,[8]]
b=[]
sum=0
for i in range(len(a)):
  if type(a[i]) is list:
    for j in range(len(a[i])):         
    #   print(i,j,a[i][j])
      b.append(a[i][j])
      sum+=a[i][j]
  else:
    # print(i,a[i])
    b.append(a[i])
    sum+=a[i]
print(b)
print(sum)
