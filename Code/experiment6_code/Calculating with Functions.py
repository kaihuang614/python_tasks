num_dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}

def zero(x=None): 
    return evaluate_expression(0, x)

def one(x=None): 
    return evaluate_expression(1, x)

def two(x=None): 
    return evaluate_expression(2, x)

def three(x=None): 
    return evaluate_expression(3, x)

def four(x=None): 
    return evaluate_expression(4, x)

def five(x=None): 
    return evaluate_expression(5, x)

def six(x=None): 
    return evaluate_expression(6, x)

def seven(x=None): 
    return evaluate_expression(7, x)

def eight(x=None): 
    return evaluate_expression(8, x)

def nine(x=None): 
    return evaluate_expression(9, x)

def plus(x):
    return '+,' + str(x)

def minus(x):
    return '-,' + str(x)

def times(x):
    return '*,' + str(x)

def divided_by(x):
    return '/,' + str(x)

def evaluate_expression(x, y):
    if y is None:
        return x
    
    operator, num = y.split(',')
    num = num_dict[num]
    
    if operator == '+':
        return x + num
    elif operator == '-':
        return x - num
    elif operator == '*':
        return x * num
    elif operator == '/':
        return int(x / num)