import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import math

from main import *
from shentan.shentan import *

sh = Shentan()

show_regression = False
num_chars = 5000
simp_char_strokes, trad_char_strokes = char_stroke_counts(num_chars,sh)
assert len(simp_char_strokes) == len(trad_char_strokes) == num_chars

information = map(lambda i: -math.log(sh.knowledge.characters.entry_by_index(i)[6] / 100,2),range(0,num_chars))

frequencies = range(len(simp_char_strokes))
simp_slope, simp_intercept, simp_r = stats.linregress(information,simp_char_strokes)[0:3]
simp_end_y = simp_intercept + simp_slope * len(simp_char_strokes)
trad_slope, trad_intercept, trad_r = stats.linregress(information,trad_char_strokes)[0:3]
trad_end_y = trad_intercept + trad_slope * len(trad_char_strokes)

print simp_r ** 2, trad_r ** 2

plt.figure(1)

plt.subplot(211)
plt.plot(simp_char_strokes,information,'.')
plt.title('Frequency vs complexity (simplified)')
if show_regression:
	plt.text(500,30,'r^2: ' + str(round(simp_r ** 2,2)))
	plt.plot([0,len(simp_char_strokes)],[simp_intercept,simp_end_y],linestyle='-',color='k',alpha=1,linewidth=5)
plt.xlabel('# of strokes')
plt.ylabel('Information content (bytes)')

plt.subplot(212)
plt.plot(trad_char_strokes,information,'g.')
plt.title('Frequency vs complexity (traditional)')
if show_regression:
	plt.text(500,30,'r^2: ' + str(round(trad_r ** 2,2)))
	plt.plot([0,len(trad_char_strokes)],[trad_intercept,trad_end_y],linestyle='-',color='k',alpha=1,linewidth=5)
plt.xlabel('# of strokes')
plt.ylabel('Information content (bytes)')

plt.show()