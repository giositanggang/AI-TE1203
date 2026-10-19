from collections import deque

# Graf sederhana yang menggambarkan jalur antar lokasi
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"]
}

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == goal:
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None

print("=== SEARCH ALGORITHM: BFS ===")
print("Lokasi tersedia:", ", ".join(graph.keys()))

start = input("Masukkan titik awal: ").strip().upper()
goal = input("Masukkan titik tujuan: ").strip().upper()

if start not in graph or goal not in graph:
    print("Error: titik tidak tersedia.")
else:
    path = bfs(graph, start, goal)

    if path:
        print("Jalur ditemukan:", " -> ".join(path))
        print("Jumlah langkah:", len(path) - 1)
    else:
        print("Jalur tidak ditemukan.")
