"""За основу взята версия deepseek"""
"""
Дано описание ориентированного графа в текстовом файле с именем FileName. в
 виде матрицы смежности. Первая строка файла содержит количество вершин графа (n), а
 следующие n строк содержат матрицу смежности (m), m[i][j]=0, если дуги из вершины i в
 вершину j не существует, иначе m[i][j] хранит вес соответствующей дуги. Выполнить
 поиск в ширину от вершины с номером k. В результате вывести номера вершин графа,
 достижимые для данной вершины, в порядке их обхода при поиске в ширину. Если на
 очередном шаге сортировки имелось несколько равноправных вершин, перечислять их в
 порядке возрастания номеров вершин.
"""

from collections import deque


def read_graph(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        graph = []
        for _ in range(n):
            row = list(map(int, file.readline().split()))
            graph.append(row)
    return graph


def bfs(graph, start):
    n = len(graph)
    visited = [False] * n
    queue = deque()
    result = []

    queue.append(start)
    visited[start] = True

    while queue:
        current = queue.popleft()
        result.append(current)

        # Получаем и сортируем соседей
        neighbors = [
            neighbor
            for neighbor in range(n)
            if graph[current][neighbor] != 0
        ]
        neighbors.sort()

        for neighbor in neighbors:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return result


def main():
    filename = "FileName"
    try:
        graph = read_graph(filename)
        n = len(graph)

        print(f"Граф содержит {n} вершин")
        prompt = f"Введите начальную вершину (0..{n - 1}): "
        k = int(input(prompt))

        if not (0 <= k < n):
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