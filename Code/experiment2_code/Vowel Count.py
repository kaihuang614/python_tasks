def get_count(sentence):
    res = 0
    for x in sentence:
        if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'): res += 1
    return res