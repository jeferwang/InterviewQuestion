"""
链接：https://www.nowcoder.com/questionTerminal/d3f26db0325444078717cc802e0056d8
来源：牛客网

小易正在玩一款新出的射击游戏,这个射击游戏在一个二维平面进行,小易在坐标原点(0,0),平面上有n只怪物,每个怪物有所在的坐标(x[i], y[i])。小易进行一次射击会把x轴和y轴上(包含坐标原点)的怪物一次性消灭。
小易是这个游戏的VIP玩家,他拥有两项特权操作:
1、让平面内的所有怪物同时向任意同一方向移动任意同一距离
2、让平面内的所有怪物同时对于小易(0,0)旋转任意同一角度
小易要进行一次射击。小易在进行射击前,可以使用这两项特权操作任意次。
小易想知道在他射击的时候最多可以同时消灭多少只怪物,请你帮帮小易。

如样例所示:

所有点对于坐标原点(0,0)顺时针或者逆时针旋转45°,可以让所有点都在坐标轴上,所以5个怪物都可以消灭。

输入描述:

输入包括三行。
第一行中有一个正整数n(1 ≤ n ≤ 50),表示平面内的怪物数量。
第二行包括n个整数x[i](-1,000,000 ≤ x[i] ≤ 1,000,000),表示每只怪物所在坐标的横坐标,以空格分割。
第二行包括n个整数y[i](-1,000,000 ≤ y[i] ≤ 1,000,000),表示每只怪物所在坐标的纵坐标,以空格分割。


输出描述:

输出一个整数表示小易最多能消灭多少只怪物。
示例1
输入

5
0 -1 1 1 -1
0 -1 -1 1 1
输出

5
"""
import time


def is_parallel(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p2[1]) == (p3[0] - p2[0]) * (p2[1] - p1[1])


def is_vertical(p1, p2, p3, p4):
    return (p2[0] - p1[0]) * (p3[0]-p4[0] ) == (p4[1] - p3[1]) * (p2[1] - p1[1])


def solve(num, point_list):
    if num < 4:
        return num
    result = 0
    for i in range(num):
        for j in range(num):
            if j != i:
                for k in range(num):
                    if k != i and k != j:
                        max_count = 3
                        for l in range(num):
                            if l != i and l != j and l != k:
                                if is_parallel(point_list[i], point_list[j], point_list[l]) or is_vertical(point_list[i], point_list[j], point_list[k], point_list[l]):
                                    max_count += 1
                        result = max(max_count, result)
    return result


if __name__ == '__main__':
    # 输入的数据
    num = int(input())
    line1 = input()
    line2 = input()
    # 处理
    line1 = [int(i) for i in line1.split(' ')]
    line2 = [int(i) for i in line2.split(' ')]
    points = []
    for i in range(num):
        points.append((line1[i], line2[i]))
    # 计算结果
    time1 = time.time()
    print(solve(num, points))
    time2 = time.time()
    print(time2 - time1)
"""
50
9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49
"""
"""
50
3 1 5 6 9 8 7 1 2 5 4 5 2 5 6 2 1 5 6 3 5 5 3 8 2 5 8 7 4 1 2 3 6 9 8 5 2 1 4 5 6 9 8 7 4 1 2 3 6 9
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49
"""
"""
9
0 -3 3 3 -3 0 0 3 -3
0 -3 -3 3 3 3 -3 0 0
"""
