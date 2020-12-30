n=int(input("Enter power of 11 : "))
l=[1,1]
print(*l[:1],sep=',')
print(*l,sep=',')
for k in range(n):
    m=[]
    for i in range(len(l)-1):
        j=i+1
        m.append(l[i]+l[j])

    m.append(1)
    m.insert(0,1)
    print(*m,sep=',')
    l=m
    
    
