import numpy as np

from shentan import *
from main import *

sh = Shentan()
sc = StrokeCountDict()

char_count = 5000

simp, trad = char_stroke_counts(char_count,sh,sc)
diff_strokes = np.array(trad) - np.array(simp)

for i in range(0,len(diff_strokes)):
	d = diff_strokes[i]
	if d < 0:
		simp = sh.knowledge.characters.entry_by_index(i)[1]
		trad = sh.jianti_to_fanti(simp)
		print simp, trad
