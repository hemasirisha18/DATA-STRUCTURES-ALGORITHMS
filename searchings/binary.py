def binarysearch(array,ele):
    l=0
    h=len(array)
    matched=False
    while l<=h and not matched:
        middle=(l+h)//2
        if array[middle]==ele:
            matched = True
        else:
            if ele<array[middle]:
                h=middle-1
            else:
                l=middle+1
    return matched

array=[24,56,1,50,17]
print(binarysearch(array,50))
