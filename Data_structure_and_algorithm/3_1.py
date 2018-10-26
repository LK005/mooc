class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def stack(self):
        return self.items
 
def calculate(s):


    opStack=Stack()
    numStack=Stack()
    prec={}
    prec['^']=4
    prec['*']=3
    prec['/']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1
    s=list(s)
    for token in s:            
        if token.isdigit():
            numStack.push(int(token))
        elif token=='(':
            opStack.push(token)
        elif token==')':
            toptoken=opStack.pop()
            while toptoken!='(':
                operand2=numStack.pop()
                operand1=numStack.pop()
                result=eval(str(operand1)+str(toptoken)+str(operand2))
                numStack.push(result)
                toptoken=opStack.pop()
        else:
            while(not opStack.isEmpty())and (prec[opStack.peek()]>=prec[token]):
                op=opStack.pop()
                operand2=numStack.pop()
                operand1=numStack.pop()
                result=eval(str(operand1)+str(op)+str(operand2))
                numStack.push(result)
            opStack.push(token)
    while not opStack.isEmpty():
        op=opStack.pop()
        operand2=numStack.pop()
        operand1=numStack.pop()
        result=eval(str(operand1)+str(op)+str(operand2))
        numStack.push(result)
    return numStack.pop()
print(calculate(input()))