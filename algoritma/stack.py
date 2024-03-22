class Stack:
  def __init__(self):
    self.stack = []
  
  def is_empty(self): # fungsi is_empty untuk mencegah error
    return True if len(self.stack) == 0 else False
  
  def push(self,item):
    self.stack.append(item)
  
  def get_stack(self): # fungsi getter untuk mendapatkan stack
    return self.stack
  
  def pop(self):
    """ pop function hanya berjalan 
    apabila list tidak kosong, selain itu mengembalikan None
    hal ini berguna untuk memastikan tidak terjadi error pada kode """
    return None if self.is_empty() else self.stack.pop() 

stack = Stack() # mendeklarasikan instance stack
print(stack.get_stack())
stack.push("A")
stack.push("B")
print(stack.get_stack())
print(stack.pop())
print(stack.get_stack())
print(stack.pop())
print(stack.get_stack())
print(stack.pop()) # harusnya menampilkan error karena stack sudah kosong