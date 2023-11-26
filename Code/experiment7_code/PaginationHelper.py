class PaginationHelper:
    def __init__(self, collection, items_per_page):
        # 初始化 PaginationHelper 类
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        # 返回集合/数组中的项目总数
        return len(self.collection)

    def page_count(self):
        # 返回分页后的总页数
        return (len(self.collection) + self.items_per_page - 1) // self.items_per_page

    def page_item_count(self, page_index):
        # 返回指定页的项目数量
        if page_index < 0 or page_index >= self.page_count():
            return -1
        
        if page_index == self.page_count() - 1:
            return len(self.collection) % self.items_per_page or self.items_per_page
        else:
            return self.items_per_page

    def page_index(self, item_index):
        # 返回包含指定项目索引的页索引
        if item_index < 0 or item_index >= len(self.collection):
            return -1
        
        return item_index // self.items_per_page