'''
Assume you have a method isSubstring which checks if one word is a substring of
another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).

'''

s1 = 'waterbottle'
s2 = 'erbottlewat'

s = s1 + s1

if s.find(s2) != -1: print 'Yes'
else: print 'No'


