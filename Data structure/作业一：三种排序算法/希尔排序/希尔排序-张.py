import math
import time
import numpy as np
np.set_printoptions(suppress=True)
compare_num = 0
swicth_num = 0
# 用来存储结果的数组
comparenum = []
swicthnum = []
run_time = []


def shell_sort(nlist):
    global compare_num
    global swicth_num
    n = len(nlist)
    gap = math.floor(n/2)
    while gap > 0:
        for i in range(gap, n):
            j = i
            temp = nlist[i]
            while j-gap >= 0 and temp < nlist[j-gap]:
                compare_num += 1
                nlist[j] = nlist[j-gap]
                swicth_num += 1
                j = j-gap
            compare_num += 1
            nlist[j] = temp
        gap = math.floor(gap/2)
    return nlist


for s in range(10, 10000, 500):
    a = np.random.randint(1, 10000, s)
    start = time.perf_counter()
    shell_sort(a)
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
np.savetxt('Shellsort_compare_num.txt', comparenum, fmt='%.0f')
np.savetxt('Shellsort_swicth_num.txt', swicthnum, fmt='%.0f')
np.savetxt('Shellsort_run_time.txt', run_time, fmt='%.4f')

