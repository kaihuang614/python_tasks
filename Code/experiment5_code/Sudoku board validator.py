def validate_sudoku(board):
    rows = [set() for _ in range(9)]  # 存储每一行中出现的数字
    cols = [set() for _ in range(9)]  # 存储每一列中出现的数字
    boxes = [set() for _ in range(9)]  # 存储每个九宫格中出现的数字

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == 0:
                return False  # 数独板中包含 0，直接返回 False 表示无效

            box_index = (i // 3) * 3 + j // 3  # 计算当前单元格所属的九宫格索引

            if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                return False  # 数字在当前行、当前列或当前九宫格中出现重复，返回 False 表示无效

            rows[i].add(num)
            cols[j].add(num)
            boxes[box_index].add(num)

    return True  # 数独板有效，返回 True