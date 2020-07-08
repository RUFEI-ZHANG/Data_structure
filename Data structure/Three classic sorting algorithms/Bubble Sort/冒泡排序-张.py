# 冒泡排序
import time
import numpy as np
compare_num = 0
swicth_num = 0
# 用来存储结果的数组
comparenum = []
swicthnum = []
run_time = []


def bubble_sort(nlist, n):
    global compare_num
    global swicth_num
    for i in range(0, n):
        for j in range(0, n-i-1):
            if nlist[j] > nlist[j+1]:
                compare_num += 1
                temp = nlist[j+1]
                nlist[j+1] = nlist[j]
                nlist[j] = temp
                swicth_num += 1
            else:
                compare_num += 1


for s in range(10, 10000, 500):
    a = np.random.randint(1, 10000, s)
    start = time.perf_counter()
    bubble_sort(a, len(a))
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
file = open('Bubblesort_compare_num.txt', 'w')
file.write(str(comparenum))
file.close()
file = open('Bubblesort_swicth_num.txt', 'w')
file.write(str(swicthnum))
file.close()
file = open('Bubblesort_run_time.txt', 'w')
file.write(str(run_time))
file.close()
