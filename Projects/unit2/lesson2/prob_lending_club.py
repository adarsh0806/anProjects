import matplotlib.pyplot as plt 
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('loansData.csv')
#clean the data
loansData.dropna(inplace = True)
#load into a dataframe
df = pd.DataFrame(loansData)
#boxplot
df.boxplot(column = 'Amount.Requested')
plt.show()
plt.savefig('AmountRequestedBOX.jpeg')
#histogram
df.hist(column = 'Amount.Requested')
plt.show()
plt.savefig('AmountRequestedHIST.jpeg')
#qqplot
plt.figure()
qqplot = stats.probplot(df['Amount.Requested'],dist = 'norm', plot = plt)
plt.show()
plt.savefig('AmountRequestedQQ.jpeg')
'''
Analysis:

Amounts in the 5000-10000 range were the most asked for values and they were the amounts 
most given by the investors as well.

'''