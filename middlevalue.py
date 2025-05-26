def middl(value):
    lenght= len(value)
    mid= lenght//2
    if lenght %2==0:
        return value[mid-1:mid+1]
    else:
        return value[mid]
l=middl('abc')
print(l)