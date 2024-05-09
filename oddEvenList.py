def change(l):
    l1=[]
    l2=[]
    for i in l:
        if i%2==0:
            l1.append(i)
        else:
            l2.append(i)
    print('even ',l1)
    print('odd',l2)

l=[1,2,3,4,5,6,7,8,9,10]
change(l)
