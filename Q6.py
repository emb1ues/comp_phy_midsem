import numpy as np

def gauss(A,b,epsilon):
    x = []
    for i in range(len(A)):
        x.append(0)
    x[0] = 1
    count=0
    temp=1
    while temp>epsilon:
        temp = 0.0
        temp1 = 0.0
        count = count + 1
        for i in range(len(x)):
            sum1 = sum2 = 0
            for j in range(1,i):
                sum1 = sum1 + A[i][j]*x[j]
            for k in range(i+1,len(x)):
                sum2 = sum2 + A[i][k]*x[k]
            temp1 = x[i]
            x[i]=(b[i]-sum1-sum2)/A[i][i]
            temp = temp + abs(temp1-x[i])
    return x


def jacob(A,b,ep):
    x = []
    for i in range(len(A)):
        x.append(0)
    d = np.diag(A)
    LU = np.array(A) - np.diagflat(d)
    sol = (b - np.dot(LU,x))/d
    while np.linalg.norm(sol - x)>ep: 
        x = sol  
        sol = (b - np.dot(LU,x))/d
    return sol

#reading the matrices
file = open('Q6_A.txt', 'r')
A = np.genfromtxt(file, delimiter='')
file.close()


file = open('Q6_b.txt', 'r')
b = np.genfromtxt(file, delimiter='')
file.close()

epsilon = 10**(-5)

xGordan = gauss(A,b,epsilon)
print("Gauss Siedel solution ",xGordan)

xJordan = jacob(A,b,epsilon)
print("Jacobi mathod soution ",xJordan)

# **************** output *************************

# Gauss Siedel solution  [1.12499983768328, -0.49999999993296457, 1.999999999977655, -1.7499999500563939, 1.000000000026814, -0.999999986681705]
# Jacobi mathod soution  [ 1.50000241 -0.5         2.         -2.49999724  1.         -1.00000147]