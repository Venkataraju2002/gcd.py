a,b=map(int,input().split())
while b!=0:
    if b%a==0:
        b=b%a
        print("gcd:",a)
        
    else:
        if a<b:
            b=b%a
        elif a>b:
            a,b=b,a
        
