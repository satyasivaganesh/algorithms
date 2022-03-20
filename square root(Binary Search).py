def sqrtN(n):
    l=1
    u=n
    while l<=u:
        m=(l+u)//2
        if m*m>n:
            u=m-1
        elif m*m<n:
            l=m+1
        else:
            return m
    return u
