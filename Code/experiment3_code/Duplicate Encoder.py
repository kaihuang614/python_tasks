def duplicate_encode(word):
    res = ""#答案
    zidian = {}#使用字典来记录每个字符在所给字符串中的出现次数
    word_lower = word.lower()#将所给字符串转换成小写字符串，避免判断大小写
    
    for x in word_lower:
        if x in zidian:#不是第一次在字典出现，累加次数
            zidian[x] += 1
        else:
            zidian[x] = 1#第一次在字典出现
            
    for x in word_lower:
        if zidian[x] > 1: res += ')'#不是第一次出现，用右括号替换
        else: res += '('#是第一次出现，用左括号替换
        
    return res