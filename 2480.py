x,y,z= map(int,input().split())
if x==y :
    if x==y==z:
        print(10000+x*1000)
    else:
        print(1000+x*100)
elif y==z:
    if x==y==z:
        print(10000+x*1000)
    else:
        print(1000+y*100)
elif z==x:
    if x==y==z:
        print(10000+x*1000)
    else:
        print(1000+z*100)
else:
    print(max(x,y,z)*100)
