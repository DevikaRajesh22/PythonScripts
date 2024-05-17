def change(p,q=30):
    p=p+q 
    q=p-q
    print(p,'#',q)
    return p
r=150
s=100
r=change(r,s)
print(r,'#',s)
s=change(s) 
print(r,'#',s)