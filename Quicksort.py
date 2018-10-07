A = [1,4,10,14,7,9,3,2,8,16]
def Quicksort(a,i,j):
    if i<j:
        dp = Partition(a,i,j)
        Quicksort(a,i,dp-1)
        Quicksort(a,dp+1,j)
def Partition(a,left,right):
    temp = a[right]
    i = left
    j = left-1
    while i < right:
        if a[i]<temp:
            j+=1
            a[i],a[j] = a[j],a[i]
        i+=1
    a[j+1],a[right] = a[right],a[j+1]
    return j+1
Quicksort(A,0,len(A)-1)
print(A)
