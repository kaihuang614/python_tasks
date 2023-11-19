COLOR = {'GG':'G', 'BB':'B', 'RR':'R', 'BR':'G', 'BG':'R', 'GB':'R', 'GR':'B', 'RG':'B', 'RB':'G'}

# 根据颜色对照表 COLOR 返回给定颜色的结果
def get_colour(colour):
    return COLOR[colour]
    
# 计算最大的幂次，使得 3^p + 1 <= length_row
def get_power(length_row):
    p = 1
    while length_row >= 3**(p)+1:
        if length_row == 3**(p)+1:
            return 3**(p)+1
        p += 1
    return 3**(p-1)+1
   
def triangle(row):
    # 如果行的长度小于 3，则直接返回行本身（如果长度为 1）或者行的首尾颜色的组合结果
    if len(row) < 3:
        return row if len(row) is 1 else get_colour(row[0]+row[-1]) 
        
    # 获取最大的幂次
    row_p = get_power(len(row))
    
    # 如果行的长度等于最大幂次，则返回行的首尾颜色的组合结果
    if len(row) == row_p:
        return get_colour(row[0]+row[row_p-1]) 
    
    # 构建新的行，通过将每个相邻的颜色组合进行转换
    new_row = ''
    for i in range(len(row)-row_p+1):
        new_row += get_colour(row[i]+row[row_p+i-1])
    
    # 递归调用 triangle 函数，对新的行进行处理
    return triangle(new_row)