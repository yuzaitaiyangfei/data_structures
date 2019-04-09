#coding:utf-8

def buble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):
        count =0#优化
        for i in range(n-1-j):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
                count+=1
        if count==0:
            return alist
    return alist

if __name__=='__main__':
    a = [25,36,93,17,77,31,44,55,20]
    print(buble_sort(a))
