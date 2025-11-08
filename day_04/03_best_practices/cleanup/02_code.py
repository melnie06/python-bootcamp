def function(ix):
    ic = {}

    for i in ix:
        if i in ic:
            ic[i] += 1
        else:
            ic[i] = 1

    return ic
