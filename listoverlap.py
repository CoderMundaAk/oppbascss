def overlap(a,b):
    # return [x for x in a if x in b]
    for x in a:
        if x in b:
            # print(list(x))
            x = (i for i in range(3))
            print(list(x))



l1=[1,2,3]
l2=[2,3,4]
ll=overlap(l1,l2)
print(ll)
