def LCS(X,Y):
    L = [[0 for i in range(len(Y)+1)]for j in range(len(X)+1)]
    
    for i in range(len(X)+1):
        L[i][0]=0
    for j in range(len(Y)+1):
        L[0][j]=0
    for i in range(1,len(X)+1):
        for j in range(1,len(Y)+1):
            if X[i-1]==Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            elif L[i-1][j] <= L[i][j-1]:
                L[i][j]=max(L[i-1][j],L[i][j-1])
    return L


def LCS_Str(L,i,j,X,Y):
    r_lcs=''
    while i>0 and j>0:
        if X[i-1]==Y[j-1]:
            r_lcs=r_lcs+X[i-1]
            i=i-1
            j=j-1
        elif L[i-1][j] <= L[i][j-1]:
            j=j-1
        else:
            i = i-1
    return r_lcs[::-1]
X = 'GTTCCTAATA'
Y = 'CGATAATTGAGA'
L=LCS(X,Y)
print(L)
K= LCS_Str(L,len(X),len(Y),X,Y)
print(K)