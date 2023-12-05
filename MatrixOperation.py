class MatOperation:
    
    def matAdd(self,A,B):
        if len(A)==len(B) and len(A[0])== len(B[0]):
            answer=[len(A[0])*[0] for i in range(len(A))]
            for i in range(0, len(A)):
                for j in range(0,len(A[0])):
                    answer[i][j]=A[i][j]+B[i][j]
            return answer
        
    def matSub(self,A,B):
        if len(A)==len(B) and len(A[0])== len(B[0]):
            answer=[len(A[0])*[0] for i in range(len(A))]
            for i in range(0, len(A)):
                for j in range(0,len(A[0])):
                    answer[i][j]=A[i][j]-B[i][j]
            return answer
        
    def matMulti(self,A,B):
        answer=[len(B[0])*[0] for i in range(len(A))]
        if len(A[0])==len(B):
            for i in range(0, len(A)):
                for j in range(0,len(B[0])):
                    for k in range(0,len(A[0])):
                        answer[i][j]+= A[i][k]*B[k][j]
            return answer
    
    def MarkovProcess(self, I , R, n):
        ret= I
        print("Initial state:")
        for i in range(n):
            ret=self.matMulti(ret,R)
            print("At Time: ", i+1, "\t", ret)
            
if __name__ == "__main__":
    A=[[1,2],[3,4]]
    B=[[1,2],[3,4]]
    mo=MatOperation()
    print(mo.matAdd(A,B))
    print(mo.matSub(A,B))
    print(mo.matMulti(A,B))
    
    I=[[0.55,0.45]]
    R=[[0.7,0.3],[0.1,0.9]]
    print(mo.MarkovProcess(I,R,5))