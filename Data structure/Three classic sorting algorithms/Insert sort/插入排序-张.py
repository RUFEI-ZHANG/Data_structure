# 直接插入排序  稳定
import time
import numpy as np
np.set_printoptions(suppress=True)
compare_num = 0
swicth_num = 0
# 用来存储结果的数组
comparenum = []
swicthnum = []
run_time = []


def insert_sort(nlist, n):
    global compare_num
    global swicth_num
    for i in range(1, n):
        t = nlist[i]
        j = i-1 
        while j >= 0 and t < nlist[j]:
            compare_num += 1
            nlist[j+1] = nlist[j]
            swicth_num += 1
            j -= 1 
        nlist[j+1] = t
        compare_num += 1

for s in range(10, 10000, 500):
    a = np.random.randint(1, 10000, s)
    start = time.perf_counter()
    insert_sort(a, len(a))
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
np.savetxt('Insertsort_compare_num.txt', comparenum, fmt='%.0f')
np.savetxt('Insertsort_swicth_num.txt', swicthnum, fmt='%.0f')
np.savetxt('Insertsort_run_time.txt', run_time, fmt='%.4f')

