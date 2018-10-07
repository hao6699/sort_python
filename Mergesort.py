A = [1,4,10,14,7,9,3,2,8,16]
def Merge(a,p,q,r):
    L = a[p:q+1]
    R = a[q+1:r+1]
    L.append(float('inf'))
    R.append(float('inf'))
    length = len(L+R)
    i = 0
    j = 0
    for k in range(length-2):
        if L[i]<R[j]:
            a[p+k] = L[i]
            i += 1
        else:
            a[p+k] = R[j]
            j += 1
def Mergesort(a,p,r):
    if p < r:
        q = (p+r)//2
        Mergesort(a,p,q)
        Mergesort(a,q+1,r)
        Merge(a,p,q,r)
Mergesort(A,0,len(A)-1)
print(A)
