# 练习2：输入圆的半径计算计算周长和面积。

"""
输入半径计算圆的周长和面积

Version: 0.1
"""

import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)