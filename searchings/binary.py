def binarysearch(array,ele):
    l=0
    h=len(array)
    middle=0
    while l<=h:
        middle=(l+h)//2
        if array[middle]==ele:
            return middle
        else:
            if ele<array[middle]:
                h=middle-1
            else:
                l=middle+1
    return -1

# sample array is given it returns the index if element is present orelse returns -1
array=[24,56,1,50,17]
print(binarysearch(array,50))
