from collections import deque

graph = [
    [0, 1, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]

weighted_graph = [
    [0, 4, 0, 2, 9, 0, 0, 0],
    [4, 0, 3, 0, 0, 0, 0, 0],
    [0, 3, 0, 8, 0, 0, 4, 0],
    [2, 0, 8, 0, 0, 6, 0, 0],
    [9, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 6, 1, 0, 0, 3],
    [0, 0, 4, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 3, 2, 0],
]


def dfs(graph, start):
  visited = set()
  order = []

  def _dfs_recursive(v):
    visited.add(v)
    order.append(v)
    for neighbor in range(len(graph)):
      if graph[v][neighbor] != 0 and neighbor not in visited:
        _dfs_recursive(neighbor)

  _dfs_recursive(start)
  return order


def bfs(graph, start):
  visited = {start}
  queue = deque([start])
  order = []

  while queue:
    v = queue.popleft()
    order.append(v)
    for neighbor in range(len(graph)):
      if graph[v][neighbor] != 0 and neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)

  return order


def dijkstra(graph, start, finish):
  n = len(graph)
  if start == finish:
    return 0, [start]

  distances = [float('inf')] * n
  distances[start] = 0
  parents = [None] * n
  visited = [False] * n

  for _ in range(n):
    min_dist = float('inf')
    u = -1
    for i in range(n):
      if not visited[i] and distances[i] < min_dist:
        min_dist = distances[i]
        u = i

    if u == -1 or u == finish:
      break

    visited[u] = True

    for v in range(n):
      weight = graph[u][v]
      if weight > 0 and not visited[v]:
        new_dist = distances[u] + weight
        if new_dist < distances[v]:
          distances[v] = new_dist
          parents[v] = u

  if distances[finish] == float('inf'):
    return None, []

  path = []
  curr = finish
  while curr is not None:
    path.append(curr)
    curr = parents[curr]
  path.reverse()

  return distances[finish], path


def shortest_path_bfs(graph, start, finish):
  if start == finish:
    return 0, [start]

  visited = {start}
  queue = deque([start])
  parents = {start: None}

  while queue:
    u = queue.popleft()
    if u == finish:
      break

    for v in range(len(graph)):
      if graph[u][v] != 0 and v not in visited:
        visited.add(v)
        parents[v] = u
        queue.append(v)

  if finish not in parents:
    return None, []

  path = []
  curr = finish
  while curr is not None:
    path.append(curr)
    curr = parents[curr]
  path.reverse()

  return len(path) - 1, path


if __name__ == '__main__':
  print('=== ЗАДАНИЕ 1: DFS ===')
  for s in [0, 4]:
    print(f'DFS от вершины {s}: {dfs(graph, s)}')

  print('\n=== ЗАДАНИЕ 2: BFS ===')
  for s in [0, 4]:
    print(f'BFS от вершины {s}: {bfs(graph, s)}')

  print('\n=== ЗАДАНИЕ 3: Алгоритм Дейкстры ===')
  for start, finish in [(0, 7), (2, 4), (3, 3)]:
    dist, path = dijkstra(weighted_graph, start, finish)
    if path:
      print(
          f'Путь ({start} -> {finish}): вес = {dist}, маршрут ='
          f" {' -> '.join(map(str, path))}"
      )
    else:
      print(f'Путь ({start} -> {finish}): недостижим')

  print('\n=== ЗАДАНИЕ 4: Сравнение BFS и Дейкстры на невзвешенном графе ===')
  for start, finish in [(0, 7), (1, 5), (2, 4)]:
    edges_bfs, path_bfs = shortest_path_bfs(graph, start, finish)
    dist_dijk, path_dijk = dijkstra(graph, start, finish)
    print(f'Пара ({start}, {finish}):')
    print(
        f'  BFS:      рёбер = {edges_bfs}, маршрут ='
        f" {' -> '.join(map(str, path_bfs))}"
    )
    print(
        f'  Дейкстра: вес   = {dist_dijk}, маршрут ='
        f" {' -> '.join(map(str, path_dijk))}"
    )
