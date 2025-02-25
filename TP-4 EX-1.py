def f(x):
    x=(x+3)%6
    print("x=",x)
def g():
    global x
    x=(x+3)%6
    print("x=",x)
def h(x):
    x=(x+3)%6
    print("x=",x)
    return x
x=17
f(x)
print("x=",x)
g()
print("x=",x)
x=h(x)
print("x=",x)