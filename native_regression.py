from matrix import *
import sys
import matplotlib.pyplot as plt

def main(filename):
    data = loadtxt(filename)
    X = transpose(data)[0]
    Y = transpose(data)[1]
    Xp  = powers(X,0,1)
    Yp  = powers(Y,1,1)
    Xpt = transpose(Xp)
    [[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    plt.plot(X,Y)
    plt.show()

main(sys.argv[1])