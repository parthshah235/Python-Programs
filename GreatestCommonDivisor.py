def GCD(A,B):
    if B==0:
        return A
    else:
        return GCD(B, A % B)
a,b=map(int,raw_input().split())
print GCD(a,b)
