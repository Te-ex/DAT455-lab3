def transpose(l):
    return list(map(list, zip(*l)))

def powers(l,start,stop):
    n = len(l)
    p = []
    for i in range(n):
        s = []
        for j in range(start,stop+1):
            s.append(l[i]**j)
        p.append(s)
    return p

def matmul(A,B):
    h = len(A)
    if len(B) == 0:
        w = 0
        n = 0
    else:
        w = len(B[0])
        n = len(B)
    C = []
    for i in range(h):
        C.append([])
        for j in range(w):
            C[i].append(0)
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
    return C

def invert(A):
    det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    return [[A[1][1]/det,-A[0][1]/det],[-A[1][0]/det,A[0][0]/det]]

def loadtxt(filename):
    fileContent = open(filename)
    A = []
    for line in fileContent:
        B = []
        row = line.split()
        for value in row:
            B.append(float(value))
        A.append(B)
    fileContent.close()
    return A
    