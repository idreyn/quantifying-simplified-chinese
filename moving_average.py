import numpy as np
import matplotlib.pyplot as plt

from main import *

simp_mean = []
trad_mean = []

counts = range(100,5000,100)

for i in counts:
	s, t = char_stroke_counts(i)
	simp_mean.append(np.mean(s))
	trad_mean.append(np.mean(t))

plt.plot(counts,trad_mean,'g',label='traditional',linewidth=2)
plt.plot(counts,simp_mean,'b',label='simplified',linewidth=2)
plt.axis([0,5000,0,20])
plt.title('Character subset size vs. mean complexity')
plt.xlabel('# most common characters')
plt.ylabel('Mean number of strokes')
plt.legend()
plt.show()
