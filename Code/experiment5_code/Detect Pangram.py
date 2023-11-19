def is_pangram(s):
    lower_s = s.lower() #因为不区分大小写所以将s转成全部小写
    str = 'abcdefghijklmnopqrstuvwxyz' #26个字母的字符串
    
    for char in str: #遍历str
        if char not in lower_s: #如果存在字母不在lower_s里面，说明s不是pangram，返回False
            return False
        
    return True #26个字母都在lower_s里面，说明s是pangram，返回True