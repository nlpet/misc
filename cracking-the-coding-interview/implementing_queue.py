'''
Implementing a queue
'''


class Queue:
  def __init__(self):
    self.data = []
    
  def push(self, element):
    self.data.append(element)
    
  def dequeue(self):
    return self.data.pop(0)
    
  def __repr__(self):
    return str(self.data)