# #!/usr/bin/env python
# import math
# c=50
# h=30
# value = []
# items=[x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
#
# print ('\n'.join(value))
#----------------------------------------#

#----------------------------------------#

# input_str = input()
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
#
# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col]= row*col
#
# print (multilist)
# #----------------------------------------#

#----------------------------------------#

# items=[x for x in input().split(',')]
# items.sort()
# print (','.join(items))
#----------------------------------------#

#----------------------------------------#

# lines = []
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;
#
# for sentence in lines:
#     print (sentence)
#----------------------------------------#

#----------------------------------------#

# s = input()
# words = [word for word in s.split(" ")]
# print (" ".join(sorted(list(set(words)))))
# #----------------------------------------#
#----------------------------------------#

# value = []
# items=[x for x in input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp%5:
#         value.append(p)
#
# print (','.join(value))
#----------------------------------------#

#----------------------------------------#

# value = []
# items=[x for x in input().split(',')]
# for p in items:
#     intp = int(p, 8)
#     if not intp%7:
#         value.append(p)
#
# print (','.join(value))
#
# #----------------------------------------#



# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print (",".join(values))
# #----------------------------------------#

#----------------------------------------#

# s = input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print ("LETTERS", d["LETTERS"])
# print ("DIGITS", d["DIGITS"])
# #----------------------------------------#

#----------------------------------------#


# s = input()
# d={"UPPER CASE":0, "LOWER CASE":0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"]+=1
#     elif c.islower():
#         d["LOWER CASE"]+=1
#     else:
#         pass
# print ("\nUPPER CASE", d["UPPER CASE"])
# print ("\nLOWER CASE", d["LOWER CASE"])
#----------------------------------------#

#----------------------------------------#


# a = input()
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# n5 = int( "%s%s%s%s%s" % (a,a,a,a,a) )
# print (n1+n2+n3+n4+n5)
#----------------------------------------#

#----------------------------------------#

# values = input()
# numbers = [x for x in values.split(",") if int(x)%2!=0]
# print (",".join(numbers))
#----------------------------------------#


# import sys
# netAmount = 0
# while True:
#     s = input()
#     if not s:
#         break
#     values = s.split(" ")
#     operation = values[0]
#     amount = int(values[1])
#     if operation=="D":
#         netAmount+=amount
#     elif operation=="W":
#         netAmount-=amount
#     else:
#         pass
# print (netAmount)
#----------------------------------------#

#----------------------------------------#

