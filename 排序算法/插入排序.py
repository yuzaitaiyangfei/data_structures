#coding:utf-8
def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    #外循环，右边无序序列中取出元素
    for i in range(1,n):
        #内循环，左边有序序列排位置
        while i>0:
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
                i -= 1
            else:
                break
    return alist
if __name__=='__main__':
    a = [25, 36, 93, 17, 77, 31, 44, 55, 20]
    print(insert_sort(a))