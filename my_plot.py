from matplotlib import pyplot
import numpy as np

# 创建一个二维数组作为示例数据
data = np.random.rand(10, 10)

# 使用 imshow 绘制热图，并指定颜色映射为 "viridis"
pyplot.imshow(data, cmap="viridis")

# 显示绘图
pyplot.show()
