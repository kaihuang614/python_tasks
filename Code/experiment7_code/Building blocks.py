class Block:
    def __init__(self, dimensions):
        # 初始化块的宽度、长度和高度属性
        self.width = dimensions[0]
        self.length = dimensions[1]
        self.height = dimensions[2]
        
    def get_width(self):
        # 返回块的宽度
        return self.width
    
    def get_length(self):
        # 返回块的长度
        return self.length
    
    def get_height(self):
        # 返回块的高度
        return self.height
    
    def get_volume(self):
        # 计算并返回块的体积
        return self.width * self.length * self.height
    
    def get_surface_area(self):
        # 计算并返回块的表面积
        return 2 * (self.width * self.length + self.width * self.height + self.length * self.height)