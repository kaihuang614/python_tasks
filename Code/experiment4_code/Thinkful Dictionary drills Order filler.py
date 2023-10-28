def fillable(stock, merch, n):
    if merch in stock: # 商品字符串在库存字典里面
        if stock[merch] >= n:   return True #库存中商品数量大于等于客户所需商品数量
        else:   return False
    return False