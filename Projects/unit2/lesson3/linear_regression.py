from scipy import stats
import collections
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import string
import statsmodels.api as sm

loansData = pd.read_csv('loansData.csv')
loansData.dropna(inplace = True)
df = pd.DataFrame(loansData)
ir =  df['Interest.Rate']
ll = df['Loan.Length']
fr = df['FICO.Range']
ar = df['Amount.Requested']
#The linear equation that fits the trend between FICO scores and interest rates
# x = []
# y = []
# for i in ir:
# 	if '%' in i:
# 		u = string.replace(i,'%','')
# 		x.append(float(u))
#print x
# 
# for i in ll:
# 	if ' months' in i:
# 		v = string.replace(i, ' months', '')
# 		y.append(int(v))
#print y
# 
# for i in fr:
# 	istring = str(i)
# 	istring.split('-')
# 	print istring

#Clean the data
clean_ir = ir.map(lambda x: float(x.rstrip('%'))/100, 4)
clean_ll = ll.map(lambda x: x.rstrip(' months'))
fs = [int(i.split('-')[0]) for i in fr]

#Update the dataframe
ir = clean_ir 
ll = clean_ll

#Add the new FICO.Score column to the dataframe
df['FICO.Score'] = fs 

#Histogram plot of FICO.Score
plt.figure()
fs = df['FICO.Score']
plot_fs = fs.hist()
#plt.show()

#generating a scatterplot matrix - a quick overview of the data we have
#a = pd.scatter_matrix(loansData, alpha = 0.05, figsize = (10,10), diagonal = 'hist')

'''
Analysis:
Trends found between  FICO Score and Interest Rate, 
No apparent trend between Monthly Income and Interest Rate. 
R-Squared. R-squared tells us how much of the variance in the data is captured by our model. 
R is a "coefficient of correlation" between the independent variables and the dependent 
variable---i.e. how much the Y depends on the separate X's. 
R lies between -1 and 1, so R2 lies between 0 and 1.
'''
#Interest rate - the dependant variable on the y axis
y = np.matrix(ir).transpose()
#Amount requested and FICO score - the independant variables
fs_x1 = np.matrix(fs).transpose()
ar_x2 = np.matrix(ar).transpose()
#put the two x axis columns together
x = np.column_stack([fs_x1,ar_x2])
#create the linear model
linear_model = sm.add_constant(x)
model = sm.OLS(y,linear_model)
f = model.fit()
print f.summary()
