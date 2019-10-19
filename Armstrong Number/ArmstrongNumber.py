import math
def ans(x):
    n=order(x)
    t_v=x
    sum1=0
    while(t_v!=0):
        a=t_v%10
        n=3
        sum1=sum1+math.pow(a,n)
        t_v=t_v/10
    return(sum1==x)
print(ans(x))
