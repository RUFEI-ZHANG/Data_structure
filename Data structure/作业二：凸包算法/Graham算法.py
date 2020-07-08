import numpy as np
import matplotlib.pyplot as plt
import imageio
from PIL import Image
import sys

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
L = 0


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str("(" + str(self.x) + ", " + str(self.y) + ")")

    def __repr__(self):
        return str(self)

    # min（）方法使用它来查找最左边/最下面的点
    def __lt__(self, other):
        return self.y < other.y or (self.y == other.y and self.x < other.x)

    def dx(self, P1):
        return P1.x - self.x

    def dy(self, P1):
        return P1.y - self.y

    def distance(self, P1):
        return np.sqrt(self.dx(P1) ** 2 + self.dy(P1) ** 2)

    def polar_angle(self, P1):
        return np.arctan2(self.dy(P1), self.dx(P1))

    @staticmethod
    def orientation(P0, P1, P2):
        return (P1.y - P0.y) * (P2.x - P1.x) - (P1.x - P0.x) * (P2.y - P1.y)
        # =0: 共线
        # >0: 顺时针
        # <0: 逆时针方向


class graham:
    def __init__(self, array):
        global L
        global point
        x, y = [], []
        a, b = [], []
        if type(array[0]) == point:
            self.points = array
        elif type(array) == str:

            with open(array) as file:
                self.points = []
                data = file.read()
                file.close()
                data = data.split(";")
                for tuples in data:
                    coords = tuples.split(",")
                    if len(coords) > 1:
                        self.points.append(point(float(coords[0]), float(coords[1])))

        self.leftmost = min(self.points)  # 输入的最低和最左点
        self.vector = [self.leftmost]
        self.vector.extend(self.__sort_points())  # 有序点的有序数组
        if len(self.vector) < 3:
            print("It's not possible to create convex hull.")
        else:
            stack = [self.vector[0], self.vector[1], self.vector[2]]
            plt.figure()

            for i in range(2, len(self.vector)):
                while point.orientation(stack[-2], stack[-1], self.vector[i]) >= 0:  # 虽然不是逆时针
                    stack.pop()  # 消除不必要的点
                stack.append(self.vector[i])  # 添加以下要点
                for point in self.points:
                    x.append(point.x)
                    y.append(point.y)
                for sta in stack:
                    a.append(sta.x)
                    b.append(sta.y)
                    plt.title("凸包算法实施过程")
                    plt.plot(x, y, "ro")
                    plt.plot(a, b)

                # a.append(self.leftmost.x)
                # b.append(self.leftmost.y)
                plt.savefig("%d.png" % (i - 2))
                plt.show()
                if i < len(self.vector) - 1:
                    a.clear()
                    b.clear()
                else:
                    a.append(self.leftmost.x)  # 添加第一个点
                    b.append(self.leftmost.y)
                    plt.plot(x, y, "ro")
                    plt.plot(a, b)
                    plt.savefig("%d.png" % (len(self.vector) - 2))
                    plt.show()
                    L = len(self.vector) - 1
            self.vector = stack
            # plt.title("凸包算法实施过程")

    def __sort_points(self):
        dic = {}
        for point in self.points:
            if point == self.leftmost:
                continue
            polar_angle = self.leftmost.polar_angle(point)  # 避免重新计算
            try:
                if self.leftmost.distance(dic[polar_angle]) < self.leftmost.distance(point):  # 如果值存在，则获取最远的值
                    dic[polar_angle] = point
            except:
                dic[polar_angle] = point  # 如果不存在，请创建它
        dic = sorted(dic.items())  # 按极角与最左边的点排序
        return [y for (x, y) in dic]  # 仅返回点，不包括polar_angles


def create_gif(image_list, gif_name, duration=2):

    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))

    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

def add_pic(s):
    imgs = []
    for n in range(0, s):
        img = str(n) + '.png'
        imgs.append(img)
    return imgs

if __name__ == "__main__":
    graham = graham("测试点集.txt")
    imgss = add_pic(L)
    create_gif(imgss, '凸包算法进行过程.gif', 1)




