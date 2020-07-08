import numpy as np
import matplotlib.pyplot as plt
import sys
import time

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str("(" + str(self.x) + ", " + str(self.y) + ")")

    def __repr__(self):
        return str(self)

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


class graham:
    def __init__(self,x,y):
        self.points = []
        for m in range(0, len(x)-1):
            self.points.append(point(float(x[m]), float(y[m])))
        self.leftmost = min(self.points)
        self.vector = [self.leftmost]
        self.vector.extend(self.__sort_points())
        if len(self.vector) < 3:
            print("It's not possible to create convex hull.")
        else:
            stack = [self.vector[0], self.vector[1], self.vector[2]]
            for i in range(3, len(self.vector)):
                while point.orientation(stack[-2], stack[-1], self.vector[i]) >= 0:
                    stack.pop()
                stack.append(self.vector[i])
            self.vector = stack

    def __sort_points(self):
        dic = {}
        for point in self.points:
            if point == self.leftmost:
                continue
            polar_angle = self.leftmost.polar_angle(point)
            try:
                if self.leftmost.distance(dic[polar_angle]) < self.leftmost.distance(
                        point):
                    dic[polar_angle] = point
            except:
                dic[polar_angle] = point
        dic = sorted(dic.items())
        return [y for (x, y) in dic]


if __name__ == "__main__":
    run_time = []
    for s in range(10, 10000, 100):
        x = np.random.randint(1, 5, s)
        y = np.random.randint(1, 5, s)
        start = time.perf_counter()
        diaoyong = graham(x, y)
        end = time.perf_counter()
        print('Running time: %.4f Seconds' % (end - start))
        run_time.append(round((end - start), 4))
    plt.title('运行时间与点集规模的关系图', size=10)
    plt.plot(range(10, 10000, 100), run_time, color='green', marker='.')
    plt.tick_params(labelsize=7)
    plt.xlabel('点集规模', size=8)
    plt.ylabel('运行时间', size=8)
    plt.savefig('运行时间与点集规模的关系图.pdf')
    plt.savefig('运行时间与点集规模的关系图.png')
    plt.show()
