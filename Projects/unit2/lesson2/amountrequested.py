import matplotlib.pyplot as plt 
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('loansData.csv')
#remove rows with null values
loansData.dropna(inplace = True)
#box plot for the loan amounts that is Amount.Funded.By.Investors
loansData.boxplot(column = 'Amount.Funded.By.Investors')
plt.show()
#histogram for the loan amounts
loansData.hist(column = 'Amount.Funded.By.Investors')
plt.show()
#QQplot for the loan amounts
plt.figure()
qqplot = stats.probplot(loansData['Amount.Funded.By.Investors'], dist = 'norm', plot = plt)
plt.show()
