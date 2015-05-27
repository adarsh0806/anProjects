from scipy import stats
import collections
import pandas as pd
import matplotlib.pyplot as plt 

loansData = pd.read_csv('loansData.csv')
loansData.dropna(inplace = True)
freq = collections.Counter(loansData['Open.CREDIT.Lines'])
print freq
plt.figure()
plt.bar(freq.keys(), freq.values(), width = 1)
plt.show()
chi, p = stats.chisquare(freq.values())
print 'Chi = ',chi
print '\np = ',p