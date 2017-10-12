#Guilherme da Rosa Ferreira
#Programação Linear

import numpy as np

def VariavelFolga( A , m , n ):
    Id = []
    for i in range( m ):
        Id.append([0.0]*( m ))
    
    for i in range( m ):
        for j in range( m ):
            if( i == j ):
                Id[i][j] = 1.0
            else:
                continue

    newA = []
    for i in range( m ):
        newA.append([0.0]*( m + n ))
            
    for i in range( m ):
        for j in range( m + n ):
            if(j < n ):
                newA[i][j] = A[i][j]
            else:
                newA[i][j] = Id[i][j-n]
    
    return ( newA )
#########################################################
def matrizBeN( A , xb , m , n , flag ):
    if flag == 0 :
        B = []
        for i in range( m ):
            B.append([0]*( m ))
    elif flag == 1 :
        N = []
        for i in range( m ):
            N.append([0]*( n ))
            
    for i in range( m ):
        l=0
        for k in range ( len(xb) ):
            for j in range( m + n ):
                if j == xb[k]-1 and flag == 0 :
                    B[i][l] = A[i][xb[l]-1]            
                    l=l+1
                elif j == xb[k]-1 and flag == 1 :
                    N[i][l] = A[i][xb[l]-1]            
                    l=l+1
    if flag == 0:
        return( B )
    elif flag == 1:
        return( N )
#########################################################
def InvB( B ):
    B = np.asarray(B)
    if np.linalg.det(B) != 0:
        inversa = np.linalg.inv(B)

    inversa = list(inversa)
    return( inversa)
#########################################################
def verificaSolucao( testeSolucao , Cn ):
    flag = 1
    for i in range(len( Cn )):
        if testeSolucao.item( i ) < 0.0:
            flag = 0
            return ( i )
            
    if flag == 1:     
        return ( -1 )
#########################################################
def testeRazao( N , invBb , entra , m ):

    razao = [0] * m
    count = 0
    for i in range( len(N) ):
        if N[i][entra] == 0:
            count = count + 1

    if count == len(N):
        return (-1) #infinito, problema ilimitado

    for i in range( len(N) ):
        if N[i][entra] == 0:
            razao[i] = np.inf
        else:
            razao[i] = invBb.item(i) / N[i][entra]

    y = np.sort( razao )
    indice = razao.index(y[next(i for i,v in enumerate(y) if v>0)])

    return( indice )
#########################################################
def CalculoXc( x , xb , m ):
    xc = [0]*(len(x)-m)

    xlinha = set( x )
    xblinha = set( xb )
    xc = xlinha.difference( xblinha ) #subtração de conjunto

    xc = list(xc)
    
    return( xc )
#########################################################
def CalculoCb( C , xb , m ):
    Cb = [0]*m
    for i in range( len(xb) ):
        Cb[i] = C[xb[i]-1]
    
    return( Cb )
#########################################################
def CalculoCn( C , xc , n ):
    Cn = [0]*n
    for i in range(len(xc)):
        Cn[i] = C[xc[i]-1]
    
    return( Cn )
#########################################################
def Simplex(A , C , b , m , n ):
    A = VariavelFolga(A, m, n)

    x = list(range(1,(n+m+1)))

    xb = [0]*m
    for i in range(m):
        xb[i] = x[n+i]

    B = []
    for i in range( m ):
        B.append([0]*(m))

    N = []
    for i in range( m ):
        N.append([0]*(n))

    Cb = [0]*m
    Cn = [0]*n

    flag = 0
    while flag != -1:
        xb = sorted(xb)

        xc = CalculoXc(x, xb, m) #calculando Xc
        xc = sorted(xc)

        Cb = CalculoCb(C, xb, m) #calculando Cb
        Cn = CalculoCn(C, xc, n) #calculando Cn

        B = matrizBeN(A,xb, m, n, 0) #calculando matriz B
        N = matrizBeN(A, xc, m, n, 1) #calculando matriz N
        
        invB = InvB(B) #calculando Inversa de B
        invBb = np.dot(invB, b) #calculando Inversa de B * b
        invBN = np.dot(invB, N) #calculando Inversa de B * N

        CbinvBN = np.dot(Cb, invBN) #calculando CbT * B-1 * N

        testeSolucao = CbinvBN - Cn #calculando CbT * B-1 * N - CnT

        teste = verificaSolucao(testeSolucao, Cn)

        if teste == -1:
            valorOtimo = np.dot(Cb,invBb.transpose())
            valorOtimo = "%.2f" % valorOtimo
            print(valorOtimo)
            flag = teste
            break

        sai = testeRazao(invBN, invBb, teste, m)
        if sai == -1:
            print("Ilimitado")
            flag = sai
            break
        
        entra = xc[teste]
        xb[sai] = entra
#########################################################
def main():
    m = int(input())
    n = int(input())

    A = []
    for i in range( m ):
        A.append([0]*(m+n))

    for i in range(m):
        while True:
            row = input()
            values = row.split(' ')
            
            if len(values) == n:
                break

        A[i] = list( map( float , values ) )

    b = [0.0]*m
    for i in range(m):
        b[i] = float(input())

    C = [0.0]*(n+m)
    for i in range(n):
        C[i] = float(input())

    Simplex(A, C, b, m, n)


if __name__ == "__main__":
    main()
