# import re
# value = []
# items=[x for x in input().split(',')]
# for p in items:
#     if len(p)<6 or len(p)>12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]",p):
#         continue
#     elif not re.search("[0-9]",p):
#         continue
#     elif not re.search("[A-Z]",p):
#         continue
#     elif not re.search("[$#@]",p):
#         continue
#     elif re.search("\s",p):
#         continue
#     else:
#         pass
#     value.append(p)
# print ("\n Match criteria of Password".join(value))
#----------------------------------------#

#----------------------------------------#


# from operator import itemgetter, attrgetter
#
# l = []
# while True:
#     s = input()
#     if not s:
#         break
#     l.append(tuple(s.split(",")))
#
# print (sorted (l, key=itemgetter(0,1,2)))
#----------------------------------------#

#----------------------------------------#


# def putNumbers(n):
#     i = 0
#     while i>n:
#         j=i
#         i=i-1
#         if j%7==0:
#             yield j
#
# for i in range (10) :
#     print (i)
# #----------------------------------------#

#----------------------------------------#

# import math
# pos = [0,0]
# while True:
#     s = input()
#     if not s:
#         break
#     movement = s.split(" ")
#     direction = movement[0]
#     steps = int(movement[1])
#     if direction=="UP":
#         pos[0]+=steps
#     elif direction=="DOWN":
#         pos[0]-=steps
#     elif direction=="LEFT":
#         pos[1]-=steps
#     elif direction=="RIGHT":
#         pos[1]+=steps
#     else:
#         pass
#
# print (int(round(math.sqrt(pos[1]**2+pos[0]**2))))
# #----------------------------------------#
#
# #----------------------------------------#




freq = {}   # frequency of words in text
line = input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
words.sort(line)

for w in words:
    print ("%s:%d" % (w,freq[w]))
