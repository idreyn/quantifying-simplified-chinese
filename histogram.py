import numpy as np
import matplotlib.pyplot as plt
import misc

from main import *

num_chars = 5000
simp, trad = char_stroke_counts(num_chars)
bins = range(1,30)

plt.figure(1)
plt.subplot(121)
plt.hist(simp, bins=bins, normed=1, facecolor='blue', alpha=0.75)
plt.xlabel('# of strokes')
plt.ylabel('Fraction of characters')
plt.subplot(122)
plt.hist(trad, bins=bins, normed=1, facecolor='green', alpha=0.75)
plt.xlabel('# of strokes')
plt.ylabel('Fraction of characters')

plt.figure(2)
plt.hist(simp, bins=bins, normed=1, facecolor='blue', edgecolor='none', alpha=0.5)
plt.hist(trad, bins=bins, normed=1, facecolor='green', edgecolor='none', alpha=0.5)
plt.xlabel('# of strokes')
plt.ylabel('Fraction of characters')

plt.show()