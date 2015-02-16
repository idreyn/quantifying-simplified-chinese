import numpy as np
import matplotlib.pyplot as plt

from main import *

def unique2d(a):
    x, y = a.T
    b = x + y * 1.0j 
    res, counts = np.unique(b,return_counts=True)
    res = map(lambda z: [z.real,z.imag],res)
    return res, counts

simp_char_strokes, trad_char_strokes = char_stroke_counts()

points, counts = unique2d(
  np.array(zip(simp_char_strokes,trad_char_strokes))
)

sc_x, tc_y = np.array(points).T

plt.scatter(sc_x,tc_y,counts)
plt.title('Stroke complexity by character')
plt.xlabel('# of strokes in simplified')
plt.ylabel('# of strokes in traditional')
plt.show()