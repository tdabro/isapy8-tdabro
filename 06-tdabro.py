
def fibon(n):
    x,y,i=1,1,1

    while i <= n:
        x, y = x + y, x
        print("y="+str(y))
        i=i+1

print(fibon(5))