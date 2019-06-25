# Source code in python3
stack = [];
top = 0;
code = input();
openBrackets = '({[';
closedBrackets= ']})';
position = 0;
positionStack = [];
error = False;
for char in code:
    position += 1;
    if (char in openBrackets) or (char in closedBrackets):
        if(char in openBrackets):
            stack.append(char);
            positionStack.append(position);
            top += 1;
        else:
            if(not stack):
                error = True;
                positionStack.append(position);
                break;
            if ((char == ')' and stack[top-1] == '(') or (char == ']' and stack[top-1] == '[') or (char == '}' and stack[top-1] == '{')):
                    del stack[top-1];
                    top -= 1;
                    positionStack.pop(-1);
                    continue;
            else:
                error = True;
                positionStack.append(position);
                break;
    else:
        continue;
if((not error) and (top == 0)):
    print("Success");
else:
    print(positionStack[-1]);