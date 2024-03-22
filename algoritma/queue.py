class Queue:
  
  def __init__(self):
    self.queue = []
  
  def is_empty(self):
    return True if len(self.queue) == 0 else False
  
  def get_queue(self):
    return self.queue
    
  def enqueue(self,item):
    self.queue.append(item)
  
  def dequeue(self):
    return None if self.is_empty() else self.queue.pop(0)
    
queue = Queue() # menginisiasi instance queue
print(queue.get_queue())
queue.enqueue("A")
queue.enqueue("B")
print(queue.get_queue())
print(queue.dequeue())
print(queue.get_queue())
print(queue.dequeue())
print(queue.get_queue())
print(queue.dequeue()) # harusnya menampilkan error karena queue sudah kosong   