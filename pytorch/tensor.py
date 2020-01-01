import numpy as np

x = np.array([[[3, 5, 9],
               [4, 6, 8],
               [8, 9, 3]],
              [[10, 40, 72],
               [29, 78, 80],
               [40, 30, 10]],
              [[100, 400, 720],
               [290, 780, 800],
               [400, 300, 100]]])

print(x)
print("A tensor is of rank %d" %(x.ndim))
