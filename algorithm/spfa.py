def spfa(n, edges):
    next = [[] for _ in range(n)]
    for i, j, l in edges:
        next[i].append([j, l + 1])
        next[j].append([i, l + 1])
    f = [float('inf') for _ in range(n)]
    f[0] = 0
    # visited = [False for _ in range(N)]
    line = [0]
    inLine = [False for _ in range(n)]
    inLine[0] = True
    while len(line) > 0:
        selected = line.pop(0)
        inLine[selected] = False
        for j, l in next[selected]:
            if f[selected] + l < f[j]:
                f[j] = f[selected] + l
                if not inLine[j]:
                    inLine[j] = True
                    line.append(j)
    return f

print(spfa(3, [[0,1,10],[0,2,1],[1,2,2]]))
