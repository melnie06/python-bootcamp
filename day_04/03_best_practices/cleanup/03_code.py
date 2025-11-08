class P:
    def __init__(x, n): x.nm = n

    def g(x): return "hi " + x.nm


class G:
    def __init__(s, p): s.p = p

    def sG(s): print(s.p.g())
