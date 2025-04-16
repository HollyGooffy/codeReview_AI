from collections import deque


def read_graph(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())  # Читаем количество вершин
        graph = []
        for _ in range(n):
            # Читаем каждую строку матрицы смежности
            row = list(map(int, file.readline().split()))
            graph.append(row)
    return graph


def bfs(graph, start):
    """Реализация поиска в ширину (BFS)"""
    n = len(graph)
    visited = [False] * n  # Массив посещенных вершин
    queue = deque()  # Очередь для BFS
    result = []  # Результат обхода

    # Начинаем с начальной вершины
    queue.append(start)
    visited[start] = True

    while queue:
        current = queue.popleft()
        result.append(current)  # Добавляем вершину в результат

        # Получаем всех соседей текущей вершины
        neighbors = []
        for neighbor in range(n):
            if graph[current][neighbor] != 0:  # Если есть дуга
                neighbors.append(neighbor)

        # Сортируем соседей по возрастанию номеров
        neighbors.sort()

        # Добавляем непосещенных соседей в очередь
        for neighbor in neighbors:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return result


def main():
    """Основная функция программы"""
    filename = input("Введите имя файла с графом: ")
    try:
        graph = read_graph(filename)
        n = len(graph)

        print(f"Граф содержит {n} вершин")
        k = int(input(f"Введите начальную вершину (0..{n - 1}): "))

        if k < 0 or k >= n:
            print("Ошибка: номер вершины вне допустимого диапазона")
            return

        reachable = bfs(graph, k)

        print("Достижимые вершины в порядке обхода BFS:")
        print(' '.join(map(str, reachable)))

    except FileNotFoundError:
        print("Ошибка: файл не найден")
    except ValueError:
        print("Ошибка: некорректный формат данных в файле")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()