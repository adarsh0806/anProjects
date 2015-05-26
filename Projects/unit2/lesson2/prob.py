import collections
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats

#frequencies, boxplot, a histogram, and a QQ-plot for the data
data = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
c = collections.Counter(data)
print c
count_sum = sum(c.values())
for k,v in c.iteritems():
	print "The frequency of item " +str(k)+ " is " + str((float(v)/count_sum))
#boxplot
plt.boxplot(data)
plt.show()
#histogram
plt.hist(data, histtype = 'bar')
plt.show()
#QQplot
plt.figure()
qqplot = stats.probplot(data, dist = 'norm', plot = plt)
plt.show()


