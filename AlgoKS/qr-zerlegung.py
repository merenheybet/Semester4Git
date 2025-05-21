import numpy as np
import math

arr = np.array([[0, 0, -1, 2],
                [0, -1 * math.sqrt(2), 3, -2],
                [-2, 6, -1, 3],
                [0, math.sqrt(2), -3, 0]])

q, r = np.linalg.qr(arr)

print(r)