#encoding: utf-8

def select_sort(alist):
    #选择排序
    n = len(alist)
    for j in range(0,n-1):
        #[0,1,2,...n-2]
        min_index = j
        for i in range(j+1,n):
            #[j,j+1,j+2,...,n-1]
            if alist[min_index]>alist[i]:
                min_index = i
        alist[j],alist[min_index] = alist[min_index],alist[j]
    return alist
if __name__=='__main__':
    a = [25, 36, 93, 17, 77, 31, 44, 55, 20]
    print(select_sort(a))