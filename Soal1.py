a = [[2,3],[5,6]]
b = [[5,7,8],[9,9,7]]
c = [[3,5],[5,6,7]]
d = [[2,4,0.5],[0.5,'4',0.2]]
def Konsistensi(n):
      x = len(n[0])
      z = 0
      for i in range(len(n)):
            if (len(n[i])== x):
                  z += 1
      if (z == len(n)):
            print("matriks konsisten")

      else:
            print("matriks tidak konsisten")
