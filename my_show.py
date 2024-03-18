from matplotlib import pyplot as plt
import numpy as np

# 创建一个 5x5 的随机灰度图像数据
image_data = np.random.rand(5, 5)

# 使用 imshow 显示图像
plt.imshow(image_data, cmap="gray")

# 显示图像
