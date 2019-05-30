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


# import datetime
# t0= datetime.datetime.now()
# a = double_pointer([2, 6, 7, 4, 4, 9, 3, 5, 2, 6, 8, 2, 1, 0, 5]*10000)
# print(a, (datetime.datetime.now()-t0).microseconds)


def reverse_pyramid(n):
    a = int((n + 1) / 2)
    new_n = []
    for i in range(n):
        new_n.append('*')
    for i in range(a):
        for j in new_n:
            print(j, end='')
        print()
        new_n[i] = ' '
        new_n[-(i+1)] = ' '


# reverse_pyramid(7)


def reverse_num(n):
    for i in range(len(n)//2):
        n[-i-1], n[i] = n[i], n[-i-1]

    return n


# print(reverse_num([1, 2, 3, 4, 5]))


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


import time
# t0 = time.time()
# print(fibonacci(35), time.time()-t0)


def fibonacci2(n):
    n0 = 0
    n1 = 1
    if n < 2:
        return n
    for i in range(n-1):
        n0, n1 = n1, n0+n1
        # print(n0, n1)
    return n1


# t1 = time.time()
# print(fibonacci2(10**6), time.time()-t1)
import math


def primeFactors(N):
    primelis = [0] * (N + 1)
    fac = []
    s = int(math.sqrt(N)) + 1
    for i in range(2, s):
        if primelis[i] == 0:
            k = i ** 2
            while k <= N:
                if primelis[k] == 0:
                    primelis[k] = i
                k += i
    print(s, primelis)
    while primelis[int(N)] > 0:
        fac.append(primelis[int(N)])
        N /= primelis[int(N)]
    fac.append(int(N))
    return fac


print(primeFactors(72))


def gcd(A, B):
    return gcd(B, A % B) if A % B != 0 else B


def helper(a, gcd0):
    while a != 1:
        gcd_temp = gcd(a, gcd0)
        if gcd(a, gcd_temp) == 1:
            return False
        a /= gcd_temp
    return True


def solution(A, B):
    # write your code in Python 3.6
    times = 0
    for a, b in zip(A, B):
        gcd0 = gcd(max(a, b), min(a, b))
        if helper(a, gcd0) and helper(b, gcd0):
            times += 1
    return times


print(solution([1], [1]))


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def helper(mid, A, k):
    sum_n = 0
    count = 0
    for i in A:
        if sum_n + i > mid:
            count += 1
            sum_n = 0
        if sum_n + i <= mid:
            sum_n += i
    return True if count + int(sum_n != 0) <= k else False


def solution(K, M, A):
    # write your code in Python 3.6
    s_a = sum(A)
    m_a = max(A)
    if K == 1:
        return s_a
    elif K >= len(A):
        return m_a
    mid = int((m_a + s_a) / 2)
    while m_a <= s_a:
        status = helper(mid, A, K)
        # print(m_a, s_a, mid, status)
        if status:
            s_a = mid - 1
            mid = int((m_a + s_a) / 2)
        else:
            m_a = mid + 1
            mid = int((m_a + s_a) / 2)


def solution(A):
    # write your code in Python 3.6
    pos = 1
    lpos = len(A) - 1
    points = A[0] + A[-1]
    maxm = -10001
    mpos = 0
    A += [0] * 5
    while pos < lpos:
        for i in range(pos, pos+6):
            if A[i] > -1:
                mpos = i
                break
            if maxm <= A[i]:
                mpos, maxm = i, A[i]
        # print(mpos, points)
        temp = A[mpos] if mpos < lpos else 0
        pos, points, maxm = (mpos+1, points + temp, -10001)
        # print(pos, points, maxm)
    return points


def solution(A):
    # write your code in Python 3.6
    B = [-1000000001] * 6
    B += A
    # print(B)
    points = 0
    for i in range(7, len(B)):
        count = -10000000001
        # print(B)
        for j in range(i-6, i):
            count = max(count, B[j])
            # print(count, B[j])
        # print('a')
        B[i] += count
    # print(B, C, A)
    return B[-1]