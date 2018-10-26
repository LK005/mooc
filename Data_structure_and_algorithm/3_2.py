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

    def items1(self):
        return self.items


def HTMLMatch(s):
    tagst = Stack()
    i = 0
    while i<=len(s)-1:
        lasttag = '/'
        if s[i] == '<':
            i += 1
            if s[i] == '/':
                i += 1
            else:
                while s[i] != '>':
                    # tagst.push(s[i])
                    # tagpop = 
                    lasttag += s[i]
                    i += 1
                tagst.push(lasttag)
        else:
            i += 1
    for i in tagst.items1():
        if i not in s:
            return False
            break
    return True

test = '<html> <head> <title>Example</title> </head> <body> <h1>Hello, world</h1> </body>'
print(HTMLMatch(test))
# print(HTMLMatch(input()))

