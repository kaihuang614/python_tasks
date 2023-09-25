def disemvowel(string_):
    res = ''
    yuan = 'aeiouAEIOU'#元音字符串包括所有元音的大小写
    for x in string_:
        if x not in yuan:
            res += x
    return res