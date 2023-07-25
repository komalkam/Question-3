class QueueUsingStacks:
    def __init__(self):
        self.stack_enqueue = [] 
        self.stack_dequeue = [] 

    def enqueue(self, item):
     
        self.stack_enqueue.append(item)

    def dequeue(self):
        if not self.stack_dequeue:
     
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())

     
        if self.stack_dequeue:
            return self.stack_dequeue.pop()
        else:
            
            return None

    def is_empty(self):
        
        return not self.stack_enqueue and not self.stack_dequeue


if __name__ == "__main__":
    queue = QueueUsingStacks()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Dequeue:", queue.dequeue())  

    queue.enqueue(4)

    print("Dequeue:", queue.dequeue())  
    print("Dequeue:", queue.dequeue()) 
    print("Dequeue:", queue.dequeue()) 

    print("Is Empty?", queue.is_empty())  
