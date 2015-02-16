import numpy as np
import matplotlib.pyplot as plt

from main import *
from shentan import *

sh = Shentan()

num_chars = 5000
simp_char_strokes, trad_char_strokes = char_stroke_counts(num_chars,sh)
diff_strokes = np.array(trad_char_strokes) - np.array(simp_char_strokes)

bands = {}

for i in range(0,len(diff_strokes)):
	d = diff_strokes[i]
	if d == 0:
		continue
	if not bands.get(d):
		bands[d] = []
	bands[d].append(sh.knowledge.characters.entry_by_index(i)[1])

for band in bands:
	print '====', band, '===='
	for char in sorted(bands[band]):
		print char