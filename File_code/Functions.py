def Binary_Search(ds,num):
    ds=Quick_Sort(ds)
    l,r=0,len(ds)-1
    while l<=r:
        mid=(l+r)//2
        if num==ds[mid]:
            return True
        elif num<ds[mid]:
            r=mid-1
        else:
            l=mid+1
    return False
def Quick_Sort(arr):
    if len(arr)==1 or len(arr)==0:
        return arr
    else:
        pivot=arr[-1]
        left = [x for x in arr[:-1] if x < pivot]
        right = [x for x in arr[:-1] if x >= pivot]
        return Quick_Sort(left)+[pivot]+Quick_Sort(right)
