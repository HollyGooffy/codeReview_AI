from collections import deque

def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(int, file.readline().strip().split()))
            matrix.append(row)
    return n, matrix

def bfs(n, matrix, start):
    visited = [False] * n
    result = []
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in range(n):
            if matrix[current][neighbor] != 0 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
        # Сортируем очередь, чтобы вершины обходились в порядке возрастания номеров
        queue = deque(sorted(queue))

    return result

def main(filename, start):
    n, matrix = read_graph_from_file(filename)
    reachable_vertices = bfs(n, matrix, start)
    print("Достижимые вершины в порядке обхода BFS:", reachable_vertices)

if __name__ == "__main__":
    filename = 'FileName'  # Замените на имя вашего файла
    start_vertex = 0  # Замените на номер стартовой вершины
    main(filename, start_vertex)
