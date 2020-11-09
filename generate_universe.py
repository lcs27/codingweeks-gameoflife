def generate_universe(size):
    s = []
    for i in range(0,size[0]):
        p = []
        for j in range(0,size[1]):
            p.append (0)
        s.append(p)
    return s