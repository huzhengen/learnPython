# 提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。

"""
将华氏温度转换为摄氏温度

Version: 0.1
"""

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))