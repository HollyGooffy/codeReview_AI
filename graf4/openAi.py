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
        order.append(u + 1)

        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                visited[v] = True
                queue.append(v)
    return order

def main():
    filename = "FileName"
    with open(filename, "r") as f:
        lines = f.readlines()

    n = int(lines[0].strip())

    graph = []
    for line in lines[1:1+n]:
        row = list(map(int, line.split()))
        graph.append(row)

    k = int(input("Введите номер начальной вершины: "))
    start_index = k - 1
    order = bfs(graph, start_index)
    print("Вершины, достижимые из вершины", k, "в порядке обхода:", order)

if __name__ == "__main__":
    main()
