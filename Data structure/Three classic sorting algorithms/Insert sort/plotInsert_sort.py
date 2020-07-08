import matplotlib.pyplot as plt
import numpy as np
x = []
for i in range(10, 10000, 500):
    x.append(i)

# 绘制比较次数与数据规模的关系折线图
plt.figure('插入排序')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.subplots_adjust(wspace=0.3, hspace=0.5)
y3 = np.loadtxt('Insertsort_compare_num.txt')
ax1 = plt.subplot(221)
plt.title('比较次数与数据规模的关系图', size=8)
plt.plot(x, y3, color='red', label='插入排序', marker='D')
plt.tick_params(labelsize=7)
plt.xlabel('数据规模', size=6)
plt.ylabel('比较次数', size=6)

# 绘制交换次数与数据规模的关系折线图
y6 = np.loadtxt('Insertsort_swicth_num.txt')
ax2 = plt.subplot(222)
plt.title('交换次数与数据规模的关系图', size=8)
plt.plot(x, y6, color='red', label='插入排序', marker='D')
plt.tick_params(labelsize=7)
plt.xlabel('数据规模', size=6)
plt.ylabel('交换次数', size=6)

# 绘制运行时间与数据规模的关系折线图
y9 = np.loadtxt('Insertsort_run_time.txt')
ax3 = plt.subplot(223)
plt.title('运行时间与数据规模的关系图', size=8)
plt.plot(x, y9, color='red', label='插入排序', marker='D')
plt.tick_params(labelsize=7)
plt.xlabel('数据规模', size=6)
plt.ylabel('运行时间', size=6)
plt.suptitle('插入排序')
plt.savefig('Insert_sort_plot.pdf')
plt.show()
