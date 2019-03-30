def flog_jump(x, leaves):
    blaetter = (set(range(1, x+1)))
    print(blaetter)
    af_s = set()
    for idx, num in enumerate(leaves):
        af_s.add(num)
        print(af_s)
        if af_s == blaetter:
            return idx
    return -1


print(flog_jump(1, [1]))

