def find_outlier(integers):
    odd = []    #odd列表保存integers中所有奇数
    even = []   #even列表保存integers中所有偶数
    
    for number in integers:
        if number % 2 == 0:     #若当前数为偶数，则加入even
            even.append(number)
        else:                   #否则当前数为奇数，加入odd
            odd.append(number)
            
    if len(odd) == 1:   #若odd的长度为1，说明离群数是奇数
        return odd[0]
    else:               #否则even的长度为1，说明离群数是偶数
        return even[0]