a= float (input("entrer un nombre"))
b= float (input("entrer un nombre"))
c= float (input("entrer un nombre"))
d= float (input("entrer un nombre"))
def minimum(x,y,z,v):
    m=min(min(x,y),min(z,v))
    print("le minimumest :",m)
minimum(a,b,c,d)