def count_developers(lst):
    res_list = list(filter(lambda x : x['continent'] == 'Europe' and x['language'] == 'JavaScript', lst)) # 答案列表存储符合条件的数据
    return len(res_list) # 返回答案列表的元素个数