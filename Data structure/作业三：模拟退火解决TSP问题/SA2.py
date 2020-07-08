import random
import numpy as np
import math
import matplotlib.pyplot as plt
num_city=30#城市总数
initial_t=120#初始温度
lowest_t=0.001#最低温度
M=150#当连续多次都不接受新的状态，开始改变温度
iteration=500#设置迭代次数



location=np.loadtxt('city_location.txt')



#==========================================
#对称矩阵，两个城市之间的距离
def distance_p2p_mat():
    dis_mat=[]
    for i in range(30):
        dis_mat_each=[]
        for j in range(30):
            dis=math.sqrt(pow(location[i][0]-location[j][0],2)+pow(location[i][1]-location[j][1],2))
            dis_mat_each.append(dis)
        dis_mat.append(dis_mat_each)
   # print(dis_mat)
    return dis_mat

#计算所有路径对应的距离
def cal_newpath(dis_mat,path):
    dis=0
    for j in range(num_city-1):
        dis=dis_mat[path[j]][path[j+1]]+dis
    dis=dis_mat[path[29]][path[0]]+dis#回家
    return dis

#==========================================
#点对点距离矩阵
dis_mat=distance_p2p_mat()
#初始路径
path=list(range(30))
#初始距离
dis=cal_newpath(dis_mat,path)
#初始温度
t_current=initial_t
#保存每次全程距离
dis_plt=[]
while (t_current>lowest_t):#外循环，改变温度
    count_m=0#M的计数
    count_iter=0#迭代次数计数
    while (count_m<M and count_iter<iteration):#内循环，连续多次不接受新的状态或者是迭代多次,跳出内循环        
        i=0
        j=0
        while(i==j):#防止随机了同一城市
            i=random.randint(1,29)
            j=random.randint(1,29)
        path_new=path.copy()
        path_new[i],path_new[j]=path_new[j],path_new[i]#任意交换两个城市的位置,产生新解
        #计算新解的距离
        dis_new=cal_newpath(dis_mat,path_new)
        #求差
        dis_delta=dis_new-dis
        #取0-1浮点随机数
        rand=random.random()
        #计算指数函数的值
        exp_d=math.exp(-dis_delta/t_current)
        #选择
        if dis_delta<0:
            path=path_new
            dis=dis_new
        elif exp_d>rand:
            path=path_new
            dis=dis_new    
        else:
            count_m=count_m+1
        dis_plt.append(dis)
        count_iter=count_iter+1
    t_current=0.99*t_current#改变温度
#外循环结束
dis_min=dis
path_min=path
print('最短距离：',dis_min)
print('最短路径：',path_min)

#画出路程迭代曲线
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False
x = np.arange(0,len(dis_plt))
plt.figure(figsize=(12,6))
plt.plot(x,dis_plt,'g--')
plt.xlabel('步数')
plt.ylabel("路程")
plt.title("路程迭代曲线")
plt.savefig("路程迭代曲线.pdf")
plt.show()


#画出最优路线
location_plt = location.copy()
for i in range(0,30):
    location_plt[i][0] = location[path[i]][0]
    location_plt[i][1] = location[path[i]][1]
row = np.array([location[path[0]][0],location[path[0]][1] ])
location_plt = np.row_stack((location_plt,row))
x = location_plt[:,0]
y = location_plt[:,1]
plt.figure(figsize=(8,4))
plt.plot(x,y,'r-o')
plt.xlabel('x坐标')
plt.ylabel("y坐标")
plt.title("路线图")
plt.savefig('最短路线图.pdf')
plt.show()



