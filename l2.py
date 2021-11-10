# 2.Convert Character Matrix to single String;
# 	The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest


test_list = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
a=test_list[0]+test_list[1]+test_list[2]
b=a
print(b)
s = ""
s = s.join(b)
print(s)

