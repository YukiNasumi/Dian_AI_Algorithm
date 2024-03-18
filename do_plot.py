# 创建数据
from matplotlib import pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 9, 16, 25]

# 绘制两条线
plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')

# 添加图例
plt.legend()

# 显示图形
plt.show()
