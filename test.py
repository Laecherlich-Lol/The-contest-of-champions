# def flog_jump(x, leaves):
#     blaetter = (set(range(1, x+1)))
#     print(blaetter)
#     af_s = set()
#     for idx, num in enumerate(leaves):
#         af_s.add(num)
#         print(af_s)
#         if af_s == blaetter:
#             return idx
#     return -1
#
#
# print(flog_jump(1, [1]))


def double_pointer(lis):
    min = lis[0]
    max = lis[0]
    p0 = 0
    p1 = 0
    for idx, num in enumerate(lis[1:]):
        if num < min:
            min = num
            p0 = idx + 1
        if num >= max:
            max = num
            p1 = idx + 1

    # print(p1, p0, max, min)
    return p0 - p1 if p0 > p1 else p1 -p0

import datetime
t0= datetime.datetime.now()
a = double_pointer([2, 6, 7, 4, 4, 9, 3, 5, 2, 6, 8, 2, 1, 0, 5]*10000)
print(a, (datetime.datetime.now()-t0).microseconds)