def quick_sort(a,start,end):
    if start>=end:
        return
    low=start
    high=end
    midvalue=a[low]
    while low<high:
        while low<high and a[high]>=midvalue:
            high-=1
        a[low]=a[high]
        while low<high and a[low]<midvalue:
            low+=1
        a[low]=a[high]
    a[low]=midvalue
    quick_sort(a,start,low-1)
    quick_sort(a,low+1,end)   

b=[22,1,5,9,33,948,45]
quick_sort(b,0,len(b)-1)
print(b)
