import matplotlib.pyplot as plt
import random, time
import numpy as np


def generate_points(number):
    x_range = 100
    y_range = 100
    points = []
    for _ in range(number):
        x = random.randint(0, x_range * 10) / 10.
        y = random.randint(0, y_range * 10) / 10.
        if (x, y) not in points:
            points.append((x, y))
    points = list(map(lambda x:np.asarray(x), points))
    return points

def polar_angle_sort(base, points):
    points.sort(key=lambda x:x[0])
    points.sort(key=lambda x:x[1])
    if base == 'default':
        base = points[0]
    for i in range(len(points)):
        if points[i].shape[0] == 2:
            points[i] = np.insert(points[i], 2, np.array([0]), axis = 0)
        points[i][2] = np.arctan2(points[i][1] - base[1], points[i][0] - base[0])
    points.sort(key=lambda x:x[2])

def get_area(triangle):
    a, b, c = triangle
    ab = b - a
    ac = c - a
    return np.abs(ab[0] * ac[1] - ab[1] * ac[0]) / 2.

def in_triangle(triangle, p):
    a, b, c = triangle
    x = [a[0], b[0], c[0]]
    y = [a[1], b[1], c[1]]
    if p[0] > max(x) or p[0] < min(x) or p[1] > max(y) or p[1] < min(y):
        return False
    s_abc = get_area(triangle)
    s_abp = get_area((a, b, p))
    s_apc = get_area((a, p, c))
    s_bpc = get_area((b, p, c))
    if np.abs(s_abc - s_abp - s_apc - s_bpc) < 1e-6:
        return True
    return False

def brute_force(points):
    hull = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            flag = True
            same_side = True
            v_ij = np.zeros(2)
            v_ij[0] = points[j][0] - points[i][0]
            v_ij[1] = points[j][1] - points[i][1]
            for p in range(len(points)):
                if p != i and p != j:
                    v_ip = np.zeros(2)
                    v_ip[0] = points[p][0] - points[i][0]
                    v_ip[1] = points[p][1] - points[i][1]
                    if flag:
                        sign = True if v_ij[0] * v_ip[1] - v_ij[1] * v_ip[0] >=0 else False
                        flag = False
                    if sign != (True if v_ij[0] * v_ip[1] - v_ij[1] * v_ip[0] >=0 else False):
                        same_side = False
                        break
            if same_side:
                if i not in hull:
                    hull.append(i)
                if j not in hull:
                    hull.append(j)
    hull = list(map(lambda x: points[x], hull))
    polar_angle_sort('default', hull)
    return hull

def graham_scan(points):
    polar_angle_sort('default', points)
    stack = points[:3].copy()
    for i in range(3, len(points)):
        while True:
            v1 = stack[-1] - stack[-2]
            v2 = points[i] - stack[-1]
            sign = v1[0] * v2[1] - v1[1] * v2[0]
            if sign < 0:
                del stack[-1]
            else:
                break
        stack.append(points[i])
    return stack

def find_index(l, t):
    for i in range(len(l)):
        if list(t) == list(l[i]):
            return i
    return -1

def divide_conquer(points):
    points.sort(key= lambda x: x[0])
    mid = int(len(points) / 2)
    l_points = points[:mid]
    r_points = points[mid:]
    l_hull = graham_scan(l_points)
    r_hull = graham_scan(r_points)
    l_hull.extend(r_hull)
    polar_angle_sort('default', l_hull)
    return graham_scan(l_hull)

def draw(points, convex_points, title, axes):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    axes.scatter(x, y, s=10)
    axes.set_title(title)
    i = 0
    for i in range(len(convex_points) - 1):
        x = [convex_points[i][0], convex_points[i + 1][0]]
        y = [convex_points[i][1], convex_points[i + 1][1]]
        axes.plot(x, y, c = 'b')
        i += 1
    axes.plot([convex_points[-1][0], convex_points[0][0]],[convex_points[-1][1], convex_points[0][1]], c='b')

def f(method, p):
    if method == 'brute force':
        return brute_force(p)
    if method == 'graham-scan':
        return graham_scan(p)
    if method == 'divide and conquer':
        return divide_conquer(p)

step = 1000
for method in ['brute force', 'graham-scan', 'divide and conquer']:
    plt.figure(figsize=(12, 8))
    plt.suptitle(method)
    for n_points in range(step, 4000 + 1, step):
        p = generate_points(n_points)
        axes = plt.subplot(2, 2, int(n_points / step))
        t1 = time.time()
        convex_hull = f(method, p)
        t2 = time.time()
        draw(p, convex_hull, 'point number:%d, elapsed time:%.2fs'%(n_points, t2-t1), axes)
    plt.show()

