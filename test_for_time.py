import matplotlib.pyplot as plt
from time import time

from functions import _min, _max, _sum, _mult


f = open('tests_for_project.txt')
f1 = open('answers_for_tests.txt')


tests = [[int(number) for number in line.split()] for line in f.readlines()]
answers = [[int(number) for number in line.split()] for line in f1.readlines()]


def main():
    x = []
    y = []
    for i in range(len(tests)):
        numbers = tests[i]
        ans = answers[i]
        start = time()
        if _min(numbers) == ans[0] and _max(numbers) == ans[1] and _sum(numbers) == ans[2] and _mult(numbers) == ans[3]:
            print('Тест ' + str(i + 1) + ' прошёл успешно')
        end = time()
        y.append(end - start)
        x.append(len(numbers))

    plt.figure(num="project_bedarev")
    plt.plot(x, y)
    plt.xlabel("Количество чисел в файлах")
    plt.ylabel("Время работа в секундах")
    plt.show()


if __name__ == "__main__":
    main()