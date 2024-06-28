import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Songti SC']  # 设置为支持中文的字体
plt.rcParams['axes.unicode_minus'] = False

# 数据
group1 = [28.536, 7.833, 7.838]
group2 = [10.247, 6.287, 6.435]

# 创建柱状图
fig, ax = plt.subplots(figsize=(10, 8))

bar_width = 0.35
indices = np.arange(len(group1))

# 绘制第一组柱状图
bar1 = ax.bar(indices, group1, bar_width, label='参数量')

# 绘制第二组柱状图，位置在第一组柱状图之后
bar2 = ax.bar(indices + bar_width, group2, bar_width, label='计算量')

# 在柱子顶端添加值
for i in indices:
    ax.text(i, group1[i], str(group1[i]), ha='center', va='bottom')
    ax.text(i + bar_width, group2[i], str(group2[i]), ha='center', va='bottom')

# 添加标签和图例

ax.set_xlabel('模型')
ax.set_ylabel('值')
ax.set_title('HRNet及改进模型的参数量和计算量对比')
ax.set_xticks(indices + bar_width / 2)
ax.set_xticklabels(('HRNet', 'HRNet-3阶段', 'BiTNet'))  # 替换为你的类别标签
ax.legend()

# 显示图形
plt.savefig('comparison.png', format='png')
plt.show()
