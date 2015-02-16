import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

from main import *

show_regression = False
num_chars = 9933
simp_char_strokes, trad_char_strokes = char_stroke_counts(num_chars)
diff_strokes = np.array(trad_char_strokes) - np.array(simp_char_strokes)

frequencies = range(len(simp_char_strokes))
simp_slope, simp_intercept, simp_r = stats.linregress(frequencies,simp_char_strokes)[0:3]
simp_end_y = simp_intercept + simp_slope * len(simp_char_strokes)
trad_slope, trad_intercept, trad_r = stats.linregress(frequencies,trad_char_strokes)[0:3]
trad_end_y = trad_intercept + trad_slope * len(trad_char_strokes)

plt.figure(1)

plt.subplot(211)
plt.plot(simp_char_strokes,'.')
plt.title('Frequency vs complexity (simplified)')
if show_regression:
	plt.text(500,30,'r^2: ' + str(round(simp_r ** 2,2)))
	plt.plot([0,len(simp_char_strokes)],[simp_intercept,simp_end_y],linestyle='-',color='k',alpha=1,linewidth=5)
plt.ylabel('# of strokes')
plt.xlabel('Frequency index')

plt.subplot(212)
plt.plot(trad_char_strokes,'g.')
plt.title('Frequency vs complexity (traditional)')
if show_regression:
	plt.text(500,30,'r^2: ' + str(round(trad_r ** 2,2)))
	plt.plot([0,len(trad_char_strokes)],[trad_intercept,trad_end_y],linestyle='-',color='k',alpha=1,linewidth=5)
plt.ylabel('# of strokes')
plt.xlabel('Frequency index')

plt.figure(2)
plt.plot(diff_strokes,'r.')
plt.title('Frequency vs degree of simplification')
plt.ylabel('# of strokes removed')
plt.xlabel('Frequency index')

plt.show()