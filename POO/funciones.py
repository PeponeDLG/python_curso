def func1():
    print("entra función 1")

def func2(a="nombre1",b="nombre2"):
    print("a->",a,"\nb->",b)

def funcAny(*args,**kargs):
    print(args)
    print(kargs)

def func3():
    a=1
    b=3
    return a+b

# func1()

# func2()
# func2("pepe","antonio")
# func2(b="pepe",a="antonio")

# funcAny(4,5,6,pepe=3,antonio="fuera")

print(func3())

print("fin de script")
#    if __name__ == "__main__":