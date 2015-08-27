
class StackWithMin:
  def __init__(self):
    self.data = []
    self.minimum = None
    
  def pop(self):
    if self.data:
      return self.data.pop()
    else:
      return []
    
  def push(self, element):
    if self.data:
      if self.minimum > element:
        self.minimum = element
    else:
      self.minimum = element
        
    self.data.append(element)
    
  def __repr__(self):
    return str(self.data)
    
  def min_element(self):
    return self.minimum