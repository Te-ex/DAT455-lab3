from numpy import *
import sys
import matplotlib.pyplot as plt

def powers(l,start,stop):
    n = len(l)
    p = []
    for i in range(n):
        s = []
        for j in range(start,stop+1):
            s.append(l[i]**j)
        p.append(s)
    return array(p)

def poly(a,x): #a is on the form where the exponential 0 comes first at a[0]
    y = 0
    degree = 0
    for i in a:
        y += i*x**degree
        degree += 1
    return y

def main(filename,n):
    data = loadtxt(filename)
    X = transpose(data)[0]
    Y = transpose(data)[1]
    Xp  = powers(X,0,n)
    Yp  = powers(Y,1,1)
    Xpt = Xp.transpose()
    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    a = a[:,0]
    X2 = linspace(X[0],X[-1],100).tolist()
    Y2 = [poly(a, i) for i in X2]
    plt.plot(X,Y,'ro')
    plt.plot(X2,Y2)
    plt.show()    

print(poly([1,2,3],2))
main(sys.argv[1],int(sys.argv[2]))