def Search(L,x):
    j=0
    n=len(L)
    while j<n and x>L[j]:
        if x<L[j] or j>=n-1:
            j=-1
            break
        j+=1
    return j

L=[1,2,4,6,7]
x=8
print(Search(L,x))