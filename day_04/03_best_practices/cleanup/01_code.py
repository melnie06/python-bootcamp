def function(s):
    ws = s.split()

    vc = 0
    vs = "aeiou"

    for w in ws:
        if any(v in w for v in vs):
            vc += 1

    return vc
