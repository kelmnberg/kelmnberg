
# notebook-python
import numpy as np

class Solve:
    """
    Simple linear-system solver:
      • optional LU decomposition (no permutation matrix)
      • Gauss elimination with partial pivoting
      • forward / backward substitution
    All methods are *silent* – they only compute.
    """
    def __init__(self, A, B):
        self.A = np.array(A, dtype=float)      # coefficient matrix
        self.B = np.array(B, dtype=float)      # right-hand side
        self.X = np.zeros_like(self.B)         # solution vector

    # ------------------------------------------------------------------ #
    # 1. Partial pivoting (used only by Gauss)
    # ------------------------------------------------------------------ #
    def _pivot(self, A, B):
        n = A.shape[0]
        for i in range(n):
            # find largest pivot in column i
            max_row = i
            for k in range(i + 1, n):
                if np.abs(A[k, i]) > np.abs(A[max_row, i]):
                    max_row = k
            # swap rows
            if max_row != i:
                A[[i, max_row]] = A[[max_row, i]]
                B[i], B[max_row] = B[max_row], B[i]

    # ------------------------------------------------------------------ #
    # 2. LU decomposition (Crout) – L·U = A, L has 1’s on diagonal
    # ------------------------------------------------------------------ #
    def SolveUL(self):
        n = self.A.shape[0]
        L = np.eye(n)                # unit lower-triangular
        U = np.zeros((n, n))         # upper-triangular
        A = self.A.copy()            # work on a copy

        for k in range(n):
            # U row k
            for j in range(k, n):
                U[k, j] = A[k, j] - L[k, :k] @ U[:k, j]

            # L column k (skip diagonal – already 1)
            for i in range(k + 1, n):
                if U[k, k] == 0:
                    raise ValueError("Zero pivot – matrix singular or needs pivoting")
                L[i, k] = (A[i, k] - L[i, :k] @ U[:k, k]) / U[k, k]

        return U , L

    # ------------------------------------------------------------------ #
    # 3. Gauss elimination → A becomes upper-triangular (in-place)
    # ------------------------------------------------------------------ #
    def gauss_elimination(self):
        n = self.A.shape[0]
        A = self.A.copy()
        B = self.B.copy()

        for i in range(n):
            self._pivot(A, B)                       # partial pivoting
            if A[i, i] == 0:
                raise ValueError("Singular matrix after pivoting")
            for j in range(i + 1, n):
                factor = A[j, i] / A[i, i]
                A[j, i:] -= factor * A[i, i:]       # eliminate column i
                B[j]    -= factor * B[i]

        self.A = A          # store triangular form back into the object
        self.B = B

    # ------------------------------------------------------------------ #
    # 4. Forward substitution  L y = b  (L lower-triangular, 1’s on diagonal)
    # ------------------------------------------------------------------ #
    def SolveDescente(self, L=None, b=None):
        if L is None: L = self.A
        if b is None: b = self.B

        n = L.shape[0]
        y = np.zeros(n)

        for i in range(n):
            y[i] = (b[i] - L[i, :i] @ y[:i]) / L[i, i]   # L[i,i] == 1 for LU

        return y

    # ------------------------------------------------------------------ #
    # 5. Backward substitution  U x = b  (U upper-triangular)
    # ------------------------------------------------------------------ #
    def SolveRemonte(self, U=None, b=None):
        if U is None: U = self.A
        if b is None: b = self.B

        n = U.shape[0]
        x = np.zeros(n)

        for i in range(n - 1, -1, -1):
            x[i] = (b[i] - U[i, i + 1:] @ x[i + 1:]) / U[i, i]

        self.X = x
        return x.copy()
    def Cholesky(self, A=None):
        if A is None:
           A = self.A
        else:
          A = np.array(A, dtype = float)
    
        print("please note that in cholesky algorthim, the matrix A is required to be symmetric definite positive !\`n")
        n = A.shape[0]
        B = np.zeros((n, n))
        for k in range(n):
          B[k ,k] = np.sqrt(A[k,k] - sum(B[k,p]**2 for p in range (k)))
          for i in range(k+1,n):
            B[i,k] =  (A[i,k] - sum(B[i,p]*B[k,p] for p in range(k))) /B[k,k]
        return B
    def SolveCholesky(self, A=None, b=None):
      if A is None: A = self.A
      if b is None: b = self.B
      C = self.Cholesky(A)
      y = self.SolveDescente(C,b)
      self.x = self.SolveRemonte(C.T,y)
      return self.x
    # ------------------------------------------------------------------ #
    # 6. High-level driver – no prompts, just solves
    # ------------------------------------------------------------------ #
    def solve(self):
        """
        Solve A x = b.
        method : "lu"  → LU decomposition
                 "g"   → Gauss elimination with pivoting
        """
        method = input("Do you want to use LU decomposition (lu) or Gauss elimination (g)? ")
        if method.lower() == "lu":
            U, L = self.SolveUL()
            y = self.SolveDescente(L, self.B.copy())
            self.X = self.SolveRemonte(U, y)
        else:                                   # Gauss
            self.gauss_elimination()
            self.X = self.SolveRemonte()        # A is already upper-triangular

        return self.X
    if __name__ == "__main__":
    A_ex = [[4, 2, 2],
            [2, 5, 1],
            [2, 1, 3]]
    b_ex = [8, -11, -3]

    solver = Solve(A_ex, b_ex)
    UL = solver.SolveUL()
    y =solver.SolveDescente(UL[1],b_ex)
    x = solver.SolveRemonte(UL[0],y)
    print(x)

    #print (UL[1]@ UL[0])
    print(solver.solve())
    print(solver.SolveCholesky(A_ex,b_ex))