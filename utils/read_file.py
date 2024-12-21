import os
def read_adj(file_name):
    if not os.path.exists(file_name):
        print("File not found")
        return None
    else:
        with open(file_name, 'r') as f:
            n = int(f.readline().strip())
            adj = []
            for i in range(n):
                line = list(map(int, f.readline().strip().split()))
                adj.append(line)
    return n, adj

def read_h(file_name):
    if not os.path.exists(file_name):
        print("File not found")
        return None
    else:
        with open(file_name, 'r') as f:
            n = int(f.readline().strip())
            h = []
            for i in range(n):
                line = list(map(int, f.readline().strip().split()))
                h.append(line)
    return h