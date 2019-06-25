# Source code in python3
import pdb;
class Stack():
    def __init__(self):
        self.stack = [];
        self.top = 0;
        self.maxStack = [];
    def push(self, element):
        self.stack.append(element);
        self.top += 1;
        if(len(self.maxStack) <= 0):
            self.maxStack.append(element);
        else:
            if(element > self.maxStack[-1]):
                self.maxStack.append(element);
            else:
                self.maxStack.append(self.maxStack[-1]);
    def pop(self):
        del self.stack[-1];
        self.top -= 1;
        del self.maxStack[-1];
    def getMax(self):
        if(not self.maxStack):
            return;
        else:
            return self.maxStack[-1];
numberOfQueries = int(input());
listOfQueries = [];
mainStack = Stack();
for i in range(0, numberOfQueries):
    query = input();
    listOfQueries.append(query);
for query in listOfQueries:
    query = query.split();
    if(query[0] == 'push'):
        mainStack.push(int(query[1]));
    elif(query[0] == 'pop'):
        mainStack.pop();
    else:
        print(mainStack.getMax());

