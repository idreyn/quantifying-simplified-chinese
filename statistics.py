import math
import numpy as np

from scipy import stats
from main import *

def displacement(ls):
	count = 0
	ls = list(ls)
	for i in range(1,len(ls)):
		j = i
		while j > 0 and ls[j-1] > ls[j]:
			ls[j-1], ls[j] = ls[j], ls[j-1]
			count += 1
			j -= 1
	return count

def max_displacement(ls):
	return displacement(list(reversed(sorted(ls))))

def disorder(ls):
	if len(ls) < 2:
		return 0.0
	d = displacement(ls)
	m = max_displacement(ls)
	return float(d) / m

if __name__ == '__main__':
	sh = Shentan() 

	num_chars = 5000

	(
		simp_char_strokes, 
		trad_char_strokes,
		as_simp_char_strokes,
		as_trad_char_strokes
	) = char_stroke_counts(num_chars,sh,isolate_simplifications=True)

	simp_char_strokes = np.array(simp_char_strokes)
	trad_char_strokes = np.array(trad_char_strokes)

	sets = (
		('simplified set',simp_char_strokes),
		('traditional set',trad_char_strokes),
		('different simplified set',as_simp_char_strokes),
		('different traditional set',as_trad_char_strokes)
	)

	print 'Stroke count statistics for most common', num_chars, 'characters:\n'

	for set in sets:
		name = set[0]
		data = set[1]
		print '=== Data for ' + name + ' ==='
		print 'size:', len(data)
		print 'mean:', np.mean(data)
		print 'std:', np.std(data)
		print 'median:', np.median(data)
		print 'mode:', stats.mode(data)[0]
		print 'max:', max(data)
		print 'min:', min(data)
		print 'disorder:', disorder(data)
		print ''
