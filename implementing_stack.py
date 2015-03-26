'''
Implementing a stack
'''


class Stack:
  def __init__(self):
    self.data = []
    
  def pop(self):
    if self.data:
      return self.data.pop()
    else:
      return []
    
  def push(self, element):
    self.data.append(element)
    
  def __repr__(self):
    return str(self.data)
   
  def __str__(self):
    print self.data
    
  def min_element(self):
    return min(self.data)
    
    

    
    
 