def heuristic(a, b):
    return abs(ord(a) - ord(b))

# BFS
def bfsMoRong(start, doThi):
    visited = set()
    queue = [start]
    visited.add(start)
    moRong = []
    while queue:
        nutHienHanh = queue.pop(0)
        moRong.append(nutHienHanh)
        for ke in doThi.get(nutHienHanh, []):
            if ke not in visited:
                visited.add(ke)
                queue.append(ke)
    return moRong

# A* + BFS
def Astar_BFS(start, end, doThi, giaTriCanh, hDinh):
    moRong = bfsMoRong(start, doThi)
    openList = [(heuristic(start, end), 0, start)]
    closeList = set()
    cha = {}
    chiPhi = {start: 0}

    while openList:
        openList.sort(key=lambda x: x[0] + x[1])  # f = g + h
        _, g, nutHienHanh = openList.pop(0)

        if nutHienHanh in closeList:
            continue

        closeList.add(nutHienHanh)

        if nutHienHanh == end:
            duong_di = []
            chiPhi_tong = 0
            while nutHienHanh != start:
                duong_di.append(nutHienHanh)
                chiPhi_tong += hDinh.get(nutHienHanh, 0)
                nutHienHanh = cha[nutHienHanh]
            duong_di.append(start)
            chiPhi_tong += hDinh.get(start, 0)
            duong_di.reverse()
            return duong_di, chiPhi_tong

        for ke in doThi.get(nutHienHanh, []):
            chiPhi_moi = g + giaTriCanh.get((nutHienHanh, ke), 1)
            if ke not in closeList or chiPhi_moi < chiPhi.get(ke, float('inf')):
                chiPhi[ke] = chiPhi_moi
                f = chiPhi_moi + heuristic(ke, end)
                openList.append((f, chiPhi_moi, ke))
                cha[ke] = nutHienHanh

    return None, 0

# Main
doThi = {
    'A': ['B', 'C'], 
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
}

giaTriCanh = {
    ('A', 'B'): 1,
    ('A', 'C'): 1,
    ('B', 'D'): 2,
    ('B', 'E'): 1,
    ('C', 'F'): 3,
    ('D', 'B'): 2,
    ('E', 'B'): 1,
    ('F', 'C'): 3
}

hDinh = {
    'A': 1,
    'B': 2,
    'C': 1,
    'D': 3,
    'E': 1,
    'F': 2
}

start = 'A'
end = 'E'

duong_di_ket_hop, chiPhi_tong = Astar_BFS(start, end, doThi, giaTriCanh, hDinh)
print("A* + BFS:", duong_di_ket_hop)
print("Chi phí:", chiPhi_tong)
