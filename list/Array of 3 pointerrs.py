class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @param C : tuple of integers
	# @return an integer
    def minimize(self, A, B, C):
        i=0
        j=0
        k=0
        mn=calc(A[0],B[0],C[0])
        while(i<len(A) and j<len(B) and k<len(C)):
            if(A[i]==min(A[i],B[j],C[k]) and i+1<len(A)):
                i+=1
            elif(B[j]==min(A[i],B[j],C[k]) and j+1<len(B)):
                j+=1
            elif(C[k]==min(A[i],B[j],C[k]) and k+1<len(C)):
                k+=1
            else:
                break
            mn=min(calc(A[i],B[j],C[k]),mn)
        return mn