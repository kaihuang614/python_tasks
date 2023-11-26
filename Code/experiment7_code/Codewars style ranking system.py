class User:
    rank_vector = [i for i in range(-8, 9) if i != 0]  # 可接受的等级范围

    def __init__(self):
        self.rank = -8  # 初始等级为-8
        self.progress = 0  # 初始进度为0

    def inc_progress(self, kata):
        if kata not in self.rank_vector:
            raise ValueError("不在指定的等级范围内")
        
        if self.rank == 8:
            progress_meter = 0  # 达到最高等级时，进度为0
        elif self.rank_vector.index(kata) == self.rank_vector.index(self.rank):
            progress_meter = self.progress + 3  # 完成与当前等级相同的活动，进度加3
        elif self.rank_vector.index(kata) == self.rank_vector.index(self.rank) - 1:
            progress_meter = self.progress + 1  # 完成比当前等级低一级的活动，进度加1
        elif self.rank_vector.index(kata) <= self.rank_vector.index(self.rank) - 2:
            progress_meter = self.progress  # 完成比当前等级低两级或更低的活动，进度不变
        elif self.rank == -1 and kata == 1:
            progress_meter = self.progress + 10  # 特殊情况：完成-1等级和1等级之间的活动，进度加10
        else:
            difference = abs(self.rank_vector.index(kata) - self.rank_vector.index(self.rank))
            progress_meter = self.progress + 10 * difference ** 2  # 根据等级差异计算进度
        
        progress_index = divmod(progress_meter, 100)
        self.progress = progress_index[1]  # 更新进度
        self.rank = self.__update_rank__(progress_index[0])  # 更新等级
        
        if self.rank == 8:
            self.progress = 0  # 达到最高等级时，进度重置为0
        
        return self.progress

    def __update_rank__(self, level=1):
        if self.rank == 8:
            return self.rank  # 已达到最高等级，不再更新
        elif self.rank_vector.index(self.rank) + level > self.rank_vector.index(8):
            self.rank = 8  # 更新等级为最高等级
        else:
            self.rank = self.rank_vector[self.rank_vector.index(self.rank) + level]  # 更新等级为下一个等级
        
        return self.rank