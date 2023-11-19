def find_senior(lst): 
    max_age = max(item['age'] for item in lst) # 最大年龄存储所给列表lst中元素字典字段'age'的最大值
    res_list = list(filter(lambda x : x['age'] == max_age, lst)) # 答案列表存储满足最大年龄的数据 用filter函数过滤lst
    return res_list # 返回答案列表