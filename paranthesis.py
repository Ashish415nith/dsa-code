i=0
def BalancedBrackets(Str):
    stack = []
    global i
    for char in Str: 
        i+=1
        if char == '{' or char == '(' or char == '[':
            stack.append(char) 
        
        elif char == '}' or char == ')' or char == ']':
            if len(stack) == 0:
                return False
            top_element = stack.pop() 
            if not Compare(top_element, char):
                return False
        else:
            continue
            
    if len(stack) != 0:
        return False
              
    return True

def Compare(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True  
    return False
 

if __name__ == "__main__" :  
    str = "()";
    if (BalancedBrackets(str)):
        print("success")
    else:
        print(i)

    
    

if __name__ == "__main__" :  
    str = "{()}";
    if (BalancedBrackets(str)):
        print("success")


