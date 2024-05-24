import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cauchy, t, norm

# 生成一些数据点
x = np.linspace(-10, 10, 1000)

# 计算柯西分布的概率密度
cauchy_pdf = cauchy.pdf(x)

# 计算t分布的概率密度（自由度为5）
t_pdf = t.pdf(x, df=5)

# 计算高斯分布的概率密度
gaussian_pdf = norm.pdf(x)

# 绘制图形
plt.plot(x, cauchy_pdf, color='red', linestyle='-', label='Cauchy Distribution')
plt.plot(x, t_pdf, color='green', linestyle='--', label='t Distribution (df=5)')
plt.plot(x, gaussian_pdf, color='blue', linestyle=':', label='Gaussian Distribution')

# 添加图例和标签
plt.legend()
plt.xlabel('x')
plt.ylabel('Probability Density')


# 显示图形
plt.show()