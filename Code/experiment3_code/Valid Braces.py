def valid_braces(string):
    str_list = []#空list模拟栈
    
    for x in string:
        if x == '(' or x == '[' or x == '{':
            str_list.append(x)#为左括号加入栈等待右括号匹配
        else:
            if x == ')' and str_list and str_list[-1] == '(': 
                str_list.pop()#出栈
            if x == ']' and str_list and str_list[-1] == '[': 
                str_list.pop()#出栈
            if x == '}' and  str_list and str_list[-1] == '{':
                str_list.pop()#出栈

    if str_list: return False#如果栈里面还有元素，说明匹配失败，返回False
    return True#栈为空，匹配成功，返回True