def naughty_or_nice(data):
    cnt1 = cnt2 = 0 #cnt1记录淘气孩子的人数，cnt2记录乖孩子的人数
    for months, days in data.items():# 遍历顶层键值对
        for k, v in days.items():# 遍历内层键值对
            if  v == "Naughty": cnt1 += 1
            else: cnt2 += 1
    if cnt1 > cnt2: return "Naughty!"
    return "Nice!"