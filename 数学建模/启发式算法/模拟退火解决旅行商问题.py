import numpy as np
import random
import math
import matplotlib.pyplot as plt


# 定义计算两城市之间的欧几里得距离的函数
def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


# 计算整个旅行的总距离
def total_distance(route, cities):
    distance = 0
    for i in range(len(route) - 1):
        distance += calculate_distance(cities[route[i]], cities[route[i + 1]])
    distance += calculate_distance(cities[route[-1]], cities[route[0]])  # 返回起点
    return distance


# 随机交换两个城市，生成新解
def swap_two_cities(route):
    new_route = route.copy()
    i, j = random.sample(range(len(route)), 2)
    new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route


# 模拟退火算法求解TSP问题
def simulated_annealing(cities, initial_temp, cooling_rate, stopping_temp):
    current_route = list(range(len(cities)))  # 初始路径
    random.shuffle(current_route)  # 随机打乱
    current_distance = total_distance(current_route, cities)

    best_route = current_route
    best_distance = current_distance

    temperature = initial_temp
    distances = []  # 用于存储每次迭代的距离

    while temperature > stopping_temp:
        new_route = swap_two_cities(current_route)
        new_distance = total_distance(new_route, cities)

        # 如果新解比当前解好，接受新解
        # 如果新解更差，以一定概率接受新解（允许跳出局部最优）
        if new_distance < current_distance or random.random() < math.exp(
                (current_distance - new_distance) / temperature):
            current_route = new_route
            current_distance = new_distance

            if current_distance < best_distance:
                best_route = current_route
                best_distance = current_distance

        distances.append(best_distance)  # 记录当前最佳距离
        temperature *= cooling_rate  # 降温

    return best_route, best_distance, distances


# 随机生成城市的坐标
def generate_cities(num_cities):
    return np.random.rand(num_cities, 2)


# 可视化路径
def plot_route(cities, route):
    route_cities = [cities[i] for i in route] + [cities[route[0]]]
    plt.plot([city[0] for city in route_cities], [city[1] for city in route_cities], 'o-')
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("TSP Route")
    plt.show()


# 主程序
if __name__ == "__main__":
    num_cities = 60  # 城市数量
    cities = generate_cities(num_cities)  # 生成城市
    initial_temp = 1000  # 初始温度
    cooling_rate = 0.997  # 降温速率
    stopping_temp = 1e-8  # 停止温度

    best_route, best_distance, distances = simulated_annealing(cities, initial_temp, cooling_rate, stopping_temp)

    print("最佳路径:", best_route)
    print("最佳距离:", best_distance)

    # 绘制路径
    plot_route(cities, best_route)

    # 绘制收敛曲线
    plt.plot(distances)
    plt.xlabel("Iteration")
    plt.ylabel("Distance")
    plt.title("Convergence")
    plt.show()
