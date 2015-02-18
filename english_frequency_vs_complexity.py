import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

from statistics import disorder

words = []
with open('data/english.csv') as file:
	for line in file:
		words.append(line)

counts = map(lambda w: len(w),words)

slope, sintercept, r = stats.linregress(range(len(counts)),counts)[0:3]

print 'r^2:', r ** 2
print 'disorder', disorder(counts)

plt.plot(counts[0:5000],'g.')
plt.xlabel('Word frequency index')
plt.ylabel('# of letters')
plt.show()