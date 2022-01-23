#Max Stack Problem

class Stack:
     def __init__(self):
         self.items = []
         self.second = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)
         if self.second:
             self.second.append(max(self.second[-1], int(item)))
         else: self.second.append(item)

     def pop(self):
         if self.items:
            return self.items.pop()
         else: return -1

     def popmax(self):
         if self.second:
             return self.second[-1]
         return -1

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

s= Stack()
print(s.isEmpty())
s.push(7)
s.push(3)
s.push(5)
s.push(6)
print(s.popmax())



