#coding: utf-8
def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return alist


if __name__ == '__main__':
    a = [25, 36, 93, 17, 77, 31, 44, 55, 20]
    print(shell_sort(a))