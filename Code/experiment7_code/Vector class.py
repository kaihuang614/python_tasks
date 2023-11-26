import math

class Vector:
    def __init__(self, components):
        # 初始化 Vector 类
        self.components = components

    def __str__(self):
        # 返回向量的字符串表示形式
        return '(' + ','.join(str(x) for x in self.components) + ')'

    def equals(self, other):
        # 检查两个向量是否相等
        return self.components == other.components

    def add(self, other):
        # 对向量进行加法运算
        if len(self.components) != len(other.components):
            raise ValueError("Cannot add vectors of different lengths")

        result = [x + y for x, y in zip(self.components, other.components)]
        return Vector(result)

    def subtract(self, other):
        # 对向量进行减法运算
        if len(self.components) != len(other.components):
            raise ValueError("Cannot subtract vectors of different lengths")

        result = [x - y for x, y in zip(self.components, other.components)]
        return Vector(result)

    def dot(self, other):
        # 计算向量的点积
        if len(self.components) != len(other.components):
            raise ValueError("Cannot calculate dot product of vectors of different lengths")

        result = sum(x * y for x, y in zip(self.components, other.components))
        return result

    def norm(self):
        # 计算向量的长度
        result = math.sqrt(sum(x ** 2 for x in self.components))
        return result