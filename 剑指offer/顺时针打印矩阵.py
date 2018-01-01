# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix:
            return None
        res = []
        while matrix:
            res += matrix.pop(0)  # 取出矩阵的第一行
            if not matrix or not matrix[0]:
                break
            matrix = self.TurnMatrix(matrix)
        return res

    def TurnMatrix(self, matrix):
        """
        对矩阵进行逆时针旋转
        :param matrix: 旧矩阵
        :return: 返回旋转后新的矩阵
        """
        c_size = len(matrix[0])
        r_size = len(matrix)
        newMatrix = []
        for c in range(c_size):
            newRow = []
            for r in range(r_size):
                newRow.append(matrix[r][c])
            newMatrix.append(newRow)
        newMatrix.reverse()
        return newMatrix


if __name__ == '__main__':
    m = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
    s = Solution()
    res = s.printMatrix(m)
    print(res)
