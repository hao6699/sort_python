A = [1,4,10,14,7,9,3,2,8,16]
def Max_Heapify(A,i):
    l = 2*i+1
    r = 2*(i+1)
    if l<= len(A)-1 and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= len(A)-1 and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        Max_Heapify(A,largest)
def Build_Max_Heap(A):
    loop = int(len(A)/2)-1
    for i in range(loop,-1,-1):
        Max_Heapify(A,i)
def Heapsort(A):
    Build_Max_Heap(A)
    B = []
    for i in range(len(A)-1,-1,-1):
        B.append(A[0])
        A[0],A[-1] = A[-1],A[0]
        A.pop()
        Max_Heapify(A,0)
    return B[::-1]

B = Heapsort(A)
print(B)
