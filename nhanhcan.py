from utils.read_file import read_adj
from utils.read_file import read_h
from utils.checkin import exist

def nhanhcan(adj, start, stop):
    open = []   #tập các đỉnh cần xét
    close = []  #tập các đỉnh đã xét
    tn = []     #tap cac dinh ke
    g = [float('inf')] * n
    f = [float('inf')] * n
    parent = [-1] * n
    g[start] = 0
    f[start] = h[start][1]
    fmin = float('inf')
    flag = False

    open.append(start)  #dua dinh start vao cuoi open

    while len(open) > 0:    #open khac rong
        current = open.pop(0)     #lay tu dau open
        print(f"\ncurrent: {current}")
        close.append(current)  # dua n vao close
        print(f"close: {close}")
        tn = []

        if current == stop:
            flag = True
            if(f[current] < fmin):
                fmin = f[current]

        #tim cac dinh ke n
        for neighbour in range(n):
            if adj[current][neighbour] != 0:
                if(f[current] < fmin and exist(open,neighbour) == False and exist(close,neighbour) == False):
                    tn.append(neighbour)
                    g[neighbour] = g[current] + adj[current][neighbour]
                    f[neighbour] = g[neighbour] + h[neighbour][1]
                    parent[neighbour] = current
                if(f[current] < fmin and exist(open,neighbour) == True):
                    g_new = g[current] + adj[current][neighbour]
                    f_new = g_new + h[neighbour][1]
                    if(f_new < f[neighbour]):
                        g[neighbour] = g_new
                        f[neighbour] = g_new
                        parent[neighbour] = current
                if (f[current] < fmin and exist(open, neighbour) == True):
                    tn.append(neighbour)
                    g[neighbour] = g[current] + adj[current][neighbour]
                    f[neighbour] = g[neighbour] + h[neighbour][1]

        print(f"tn: {tn}")

        # sap xep tn theo h
        tn_sorted = sorted(tn, key=lambda x: f[x])
        print(f"tn sorted: {tn_sorted}")

        open = tn_sorted + open
        print(f"open: {open}")

    if (flag):
        print("Tim thay duong di ngan nhat")
        # in ra lo trinh
        path = []
        idx = stop
        while idx != -1:
            path.insert(0, idx)
            idx = parent[idx]
        print(f"path: {path}")
        return
    else:
        print("Không tìm thấy đường đi")

if __name__ == '__main__':
    n, adj = read_adj('inputs/nc.adj')
    print(f"Number of nodes: {n}")
    for i in range(n):
        print(f"{adj[i]}")

    h = read_h('inputs/nc.h')
    for i in range(n):
        print(f"{h[i]}")

    nhanhcan(adj, 0, 1)