def recoverSecret(triplets):
    res = list({i for t in triplets for i in t})#根据triplets生成原字符串的字符列表，无重复，但非按顺序。
    for t in triplets * 2:#循环遍历triplets，每次循环按三字符列表中的顺序调整res中字符顺序。
        fix(res, t[0], t[1])
        fix(res, t[1], t[2])
    return ''.join(res)

def fix(t, a, b):
    if t.index(a) > t.index(b):
        t.remove(a)
        t.insert(t.index(b), a)