from collections import deque

def bfs(graph, start):
    n = len(graph)
    visited = [False] * n
    order = []
    queue = deque()

    visited[start] = True
    queue.append(start)

    while queue:
        u = queue.popleft()
        # Приводим индекс к нумерации вершин от 1 до n для вывода
        order.append(u + 1)

        # Проходим по всем вершинам в порядке возрастания номера
        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                visited[v] = True
                queue.append(v)
    return order

def main():
    # Чтение графа из файла 'FileName'
    filename = "FileName"
    with open(filename, "r") as f:
        lines = f.readlines()

    # Первая строка файла содержит число вершин графа
    n = int(lines[0].strip())

    # Чтение матрицы смежности – следующие n строк
    graph = []
    for line in lines[1:1+n]:
        # Принимается, что числа разделены пробелами
        row = list(map(int, line.split()))
        graph.append(row)

    # Ввод номера начальной вершины (нумерация с 1)
    k = int(input("Введите номер начальной вершины: "))

    # Преобразуем номер в индекс (т.к. индексация начинается с 0)
    start_index = k - 1

    # Выполняем поиск в ширину (BFS)
    order = bfs(graph, start_index)

    # Вывод результата
    print("Вершины, достижимые из вершины", k, "в порядке обхода:", order)

if __name__ == "__main__":
    main()
