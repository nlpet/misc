'''
Implement an algorithm to determine if a string has all unique characters. What if you
can not use additional data structures?
'''

strs = ['abcd','aaaa','acde','accc']

def check_all_unique_charcters(s):
  if len(set(s)) == len(s): return True
  else: return False
  
  
if __name__ == '__main__':
  for s in strs:
    if check_all_unique_charcters(s):
      print 'String %s contains all unique chars'
    else:
      print 'String %s does not contain all unique chars'