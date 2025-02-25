def logarithme(a):
    n=0
    while 2**n<=a:
           n=n+1
    return n
x=int(input("donner la valeur de a"))
print("la valeur de n=",logarithme(x))