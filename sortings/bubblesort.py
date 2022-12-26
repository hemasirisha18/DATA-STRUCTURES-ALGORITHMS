def bs(a):
    b=len(a)-1
    for i in range(b):
        for j in range(b-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

# sample list:
m=[90,89,3,6,56,67]
print(bs(m))