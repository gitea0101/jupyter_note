def asd0(a):
    b=1
    for i in range(1,a+1):
        b = b*i
    r = [[] for i in range(b)]
    a0=a
    b0=b
    n=1
    
    c0 = []
    for j in range(1,a0+1):
        c0.append(j)
            
    asd(a,b,c0,n,a0,b0,r)
    return r

def asd(a,b,c0,n,a0,b0,r):
    
    for i in range(a*b):
        
        c = c0[:]
        
        if(n>b0):
            ac = r[(n-1)%b0][0:((n-1)//b0)]

            for i in ac:
                c.remove(i)

        d = c[int(((n-1)%b)//(b/a))]
        r[(n-1)%b0].append(d)
            
        n = n+1
        
        
        if (n-1) % b0 == 0:
            a= a-1
            b=1
            for i in range(1,a+1):
                b = b*i
    return r
asd0(3)