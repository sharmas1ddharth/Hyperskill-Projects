
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
ops = ['+', '*', '-', '/']


while True:
    print(msg_0)
    user_input = input().split()
    x = user_input[0]
    op = user_input[1]
    y = user_input[2]
    
    def check_float(n):
        try:
            float(n)
            return True
        
        except ValueError:
            return False
        
        

    if  check_float(x) == False or check_float(y) == False:
        print(msg_1)
        continue

    elif op not in ops:    
        print(msg_2)
        continue

    elif y == '0' and op == '/':
        print(msg_3)
        continue
    
    elif op == '+':
        result = float(x) + float(y)
        
    elif op == '-':
        result = float(x) - float(y)
    
    elif op == '*':
        result = float(x) * float(y)
        
    elif op == '/' and y != 0:
        result = float(x) / float(y)
        

    print(float(result))
    break