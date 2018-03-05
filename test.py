import numpy as np
import pr5
import pr4
import time
import matplotlib.pyplot as plt

A = np.array([[2.16, 1.96, 1.56], [3.55, 3.23, 2.78], [4.85, 4.47, 3.97]])
B = np.array([13.16, 21.73, 29.75])

# Получить зависимости временных затрат от размера системы
# и типа представления (float, double, long double) коэффициентов.
times = []
times_float = []
times_double = []

times_j = []
times_float_j = []
times_double_j = []

for size in range(3, 20):
    a = np.random.rand(size, size)
    b = np.random.rand(size)

    exec_time = time.clock()
    pr4.g_ps(a, b)
    times.append((size, time.clock() - exec_time))

    exec_time = time.clock()
    pr5.j_g(a, b)
    times_j.append((size, time.clock() - exec_time))

    # Время для типа float32
    f_a = np.float32(a)
    f_b = np.float32(b)

    exec_time = time.clock()
    pr4.g_ps(f_a, f_b)
    times_float.append((size, time.clock() - exec_time))

    exec_time = time.clock()
    pr5.j_g(f_a, f_b)
    times_float_j.append((size, time.clock() - exec_time))

    # Время для типа double
    f_a = np.double(a)
    f_b = np.double(b)

    exec_time = time.clock()
    pr4.g_ps(f_a, f_b)
    times_double.append((size, time.clock() - exec_time))

    exec_time = time.clock()
    pr5.j_g(f_a, f_b)
    times_double_j.append((size, time.clock() - exec_time))

plt.grid(True)
plt.plot([time for size, time in times], [size for size, time in times],
         [time for size, time in times_j], [size for size, time in times_j])
plt.xlabel("Время")
plt.ylabel("Размер матрицы")
plt.legend(['Метод Гаусса с частичным выбором ведущего элемента', 'Метод Гаусса — Жордана'])
plt.title('Зависимости временных затрат от размера системы')
plt.show()

plt.grid(True)
plt.plot([time for size, time in times_float], [size for size, time in times_float],
         [time for size, time in times_float_j], [size for size, time in times_float_j])
plt.xlabel("Время")
plt.ylabel("Размер матрицы")
plt.legend(['Метод Гаусса с частичным выбором ведущего элемента', 'Метод Гаусса — Жордана'])
plt.title('Зависимости временных затрат от размера системы для типа Float32')
plt.show()

plt.grid(True)
plt.plot([time for size, time in times_double], [size for size, time in times_double],
         [time for size, time in times_double_j], [size for size, time in times_double_j])
plt.xlabel("Время")
plt.ylabel("Размер матрицы")
plt.legend(['Метод Гаусса с частичным выбором ведущего элемента', 'Метод Гаусса — Жордана'])
plt.title('Зависимости временных затрат от размера системы для типа Double')
plt.show()

# print(pr4.g_ps(A, B))
# print(pr5.j_g(A, B))

