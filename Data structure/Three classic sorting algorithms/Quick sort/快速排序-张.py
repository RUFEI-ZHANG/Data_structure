# 快速排序
import time
import numpy as np
np.set_printoptions(suppress=True)
compare_num = 0
swicth_num = 0
# 用来存储结果的数组
comparenum = []
swicthnum = []
run_time = []

# 定义快速排序算法


def quick_sort(nlist, low, high):
    global compare_num
    global swicth_num
    if low < high:
        i = low
        j = high
        t = nlist[low]
        while i < j:
            while i < j and nlist[j] > t:
                compare_num += 1
                j -= 1
            if i < j:
                nlist[i] = nlist[j]
                swicth_num += 1
                i += 1        
            while i < j and nlist[i] <= t:
                compare_num += 1
                i += 1
            if i < j:
                nlist[j] = nlist[i]
                swicth_num += 1
                j -= 1
        nlist[i] = t
        quick_sort(nlist, low, i-1)
        quick_sort(nlist, i+1, high)

# 设定循坏，进行不同规模的排序


for s in range(10, 10000, 500):
    a = np.random.randint(1, 10000, s)
    start = time.perf_counter()
    quick_sort(a, 0, len(a)-1)
    end = time.perf_counter()
    print(a)
    print('Compare number: %s Times' % compare_num)
    print('Swicth number: %s Times' % swicth_num)
    print('Running time: %.4f Seconds' % (end-start))
    comparenum.append(compare_num)
    swicthnum.append(swicth_num)
    run_time.append(round((end - start), 4))
    compare_num = 0
    swicth_num = 0
# 以数组的形式输出结果
print('Set of Compare number: %s' % comparenum)
print('Set of Swicth number: %s' % swicthnum)
print('Set of Run time: %s' % run_time)
# 将结果数组保存为文本，方便最终三种排序方法统一绘图
np.savetxt('Quicksort_compare_num.txt', comparenum, fmt='%.0f')
np.savetxt('Quicksort_swicth_num.txt', swicthnum, fmt='%.0f')
np.savetxt('Quicksort_run_time.txt', run_time, fmt='%.4f')


