def spin_words(sentence):
    tmp = sentence.split(' ') #将所给字符串以空格为分割符分割单词保存到列表
    res = [word[::-1] if len(word) >= 5 else word for word in tmp] #反转长度大于等于5的单词
    return ' '.join(res) #每连接1个单词加一个空格