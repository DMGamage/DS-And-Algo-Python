class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_Node = Node(value)
        self.head = new_Node
        self.tail = new_Node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next

    def add(self,value):
        new_Node = Node(value)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            new_node.prev = self.tail
            self.tail = new_Node
        self.length +=1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        self.tail  = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -=1

        if self.length ==0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self,value):
        new_Node = Node(value)

        if self.length ==0:
            self.head = new_Node
            self.tail = new_Node
        else:
            new_Node.next = self.head
            self.head.prev = new_Node
            self.head = new_Node
        self.length +=1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else :
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -=1
        return temp

    def get(self,index):
        if index < 0 or index >= self.length :
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else :
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.prev
            return temp
        
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index <0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.add(value)
        

        new_Node = Node(value)
        before = self.get(index-1)
        after = before.next

        new_Node.prev = before
        new_Node.next = after
        before.next = new_Node
        after.prev = new_Node

        self.length +=1
        return True

   


    



        
    