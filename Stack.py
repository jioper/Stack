class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return  self.items[-1]
    def size(self):
        return len(self.items)
def main():
    s=Stack()
    print(s.isEmpty())
    s.push(4)
    s.push('Youkinoshita Youkino')
    print(s.peek())
    print(s.size())
    print(s.isEmpty())
    s.push('Yuigahama Yui')
    print(s.pop())
    print(s.pop())
    print(s.size())
if __name__ == '__main__':
        main()