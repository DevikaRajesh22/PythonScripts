def modInt(l):
    l1=[]
    for i in l:
        if i%5==0:
            l1.append(i+10)
        else:
            l1.append(i)
    print(l1)

list=[2,5,3,10]
modInt(list)