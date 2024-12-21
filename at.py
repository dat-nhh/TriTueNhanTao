from utils.read_file import read_adj
from utils.read_file import read_h
from utils.checkin import exist

def at(adj, start, stop):
    open = []   #tập các đỉnh cần xét
    close = []  #tập các đỉnh đã xét
    tn = []     #tap cac dinh ke
    g = [float('inf')] * n
    parent = [-1] * n
    g[start] = h[start][1]

    open.append(start)  #dua dinh start vao cuoi open

    while len(open) > 0:    #open khac rong
        current = open.pop(0)     #lay tu dau open
        print(f"\ncurrent: {current}")
        close.append(current)  # dua n vao close
        print(f"close: {close}")
        tn = []

        if current == stop:
            print("Tim thay duong di ngan nhat")
            #in ra lo trinh
            path = []
            idx = stop
            while idx != -1:
                path.insert(0,idx)
                idx = parent[idx]
            print(f"path: {path}")
            return

        #tim cac dinh ke n
        for neighbour in range(n):
            if adj[current][neighbour] == 1 and exist(open,neighbour) == False and exist(close,neighbour) == False:
                g[neighbour] = g[current] + h[neighbour][1]
                tn.append(neighbour)
                parent[neighbour] = current
        print(f"tn: {tn}")

        open = tn + open
        print(f"open: {open}")

        # sap xep open theo h
        open = sorted(open, key=lambda x: g[x])
        print(f"open sorted: {open}")

    print("Không tìm thấy đường đi")

if __name__ == '__main__':
    n, adj = read_adj('inputs/at.adj')
    print(f"Number of nodes: {n}")
    for i in range(n):
        print(f"{adj[i]}")

    h = read_h('inputs/at.h')
    for i in range(n):
        print(f"{h[i]}")

    at(adj, 0, 19)