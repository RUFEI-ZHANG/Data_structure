import matplotlib.pyplot as plt
import numpy as np
x = []
for i in range(10, 10000, 500):
    x.append(i)

# 绘制比较次数与数据规模的关系折线图
plt.figure('快速排序')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.subplots_adjust(wspace=0.3, hspace=0.5)
y1 = np.loadtxt('Quicksort_compare_num.txt')
ax1 = plt.subplot(221)
plt.title('比较次数与数据规模的关系图', size=8)
plt.plot(x, y1, color='skyblue', label='快速排序', marker='*')
plt.tick_params(labelsize=7)
plt.xlabel('数据规模', size=6)
plt.ylabel('比较次数', size=6)

# 绘制交换次数与数据规模的关系折线图
y4 = np.loadtxt('Quicksort_swicth_num.txt')
ax2 = plt.subplot(222)
plt.title('交换次数与数据规模的关系图', size=8)
plt.plot(x, y4, color='skyblue', label='快速排序', marker='*')
plt.tick_params(labelsize=7)
plt.xlabel('数据规模', size=6)
plt.ylabel('交换次数', size=6)

# 绘制运行时间与数据规模的关系折线图
y7 = np.loadtxt('Quicksort_run_time.txt')
ax3 = plt.subplot(223)
plt.title('运行时间与数据规模的关系图', size=8)
plt.plot(x, y7, color='skyblue', label='快速排序', marker='*')
plt.tick_params(labelsize=7)
plt.xlabel('数据规模', size=6)
plt.ylabel('运行时间', size=6)
plt.suptitle('快速排序')
plt.savefig('Quick_sort_plot.png')
plt.show()
