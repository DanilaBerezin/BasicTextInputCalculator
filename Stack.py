
class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.isEmpty()
        False
        >>> x.push(15)
        >>> x
        Top:Node(15)
        Stack:
        15
        4
        2
        >>> x.peek()
        15
        >>> x
        Top:Node(15)
        Stack:
        15
        4
        2
    '''
    class Node:
        def __init__(self, value):
            self.value = value  
            self.next = None 
    
        def __str__(self):
            return "Node({})".format(self.value) 

        __repr__ = __str__
    
    def __init__(self):
        # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self.top = None
        self.count=0
    
    def __str__(self):
        # YOU ARE NOT ALLOWED TO MODIFY THE THIS METHOD
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.top == None:
            return True
        return False

    def __len__(self): 
        # YOUR CODE STARTS HERE
        temp = self.top
        c = 0
        while temp:
            c += 1
            temp = temp.next
        return c

    def push(self,value):
        # YOUR CODE STARTS HERE
        newNode = self.Node(value)
        if len(self) == 0:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
     
    def pop(self):
        # YOUR CODE STARTS HERE
        if len(self) == 0:
            return None
        if len(self) == 1:
            value = self.top.value
            self.top = None
            return value
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        # YOUR CODE STARTS HERE
        if len(self) == 0:
            return None
        return self.top.value
