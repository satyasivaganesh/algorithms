    def equilibriumPoint(self,A, N):
        t1=[0]*N
        t1[0]=A[0]
        t2=[0]*N
        t2[-1]=A[-1]
        for i in range(1,N):
            t1[i]=A[i]+t1[i-1]
        if t2[N-1]==t1[N-1]:
            return N
        for j in range(N-2,-1,-1):
            t2[j]=A[j]+t2[j+1]
            if t2[j]==t1[j]:
               return j+1
        return -1
