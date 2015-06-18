import pandas as pd
import matplotlib.pyplot as plt
import sqlite3 as lite
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import statsmodels.formula.api as smf

#importing data
df = pd.read_excel('rollingsales_manhattan.xls', skiprows = 4, nrows = 5)

#cleaning the data
#consider properties with a non zero 'sale price' and non zero 'GROSS SQUARE FEET'
df = df[df['GROSS SQUARE FEET'] > 0]
df = df[df['SALE PRICE'] > 0]

#Linear regression of SALE PRICE vs GROSS SQUARE FEET
'''
http://www.datarobot.com/blog/ordinary-least-squares-in-python/
linear model. A linear model is a model in which the dependent variable varies 
linearly with the independent variable. In other words, the dependent variable 
is directly proportional to the independent variable.
'''
#Linear Model 1

#Dependent variable - Y AXIS - SALE PRICE :response
y = np.matrix(df['SALE PRICE']).transpose()
#Independent variable - X AXIS - GROSS SQUARE FEET :predictor
x = np.matrix(df['GROSS SQUARE FEET']).transpose()

#Constant term appended to the independent variable column(the predictor column)
X = sm.add_constant(x)

#Response - y, Predictor - X
est = sm.OLS(y,X)
est = est.fit()
#print est.summary()
print 'Linear model 1'
print 'Square feet coefficient: ', est.params[1]
print 'Intercept: ', est.params[0]
print 'P-Values: ', est.pvalues
print 'R-Squared: ', est.rsquared

#visualization
# plt.figure()
# sns.jointplot('GROSS SQUARE FEET', 'SALE PRICE', df, kind = 'reg')
# plt.show()

#Linear model 2

#log(SALE PRICE) vs GROSS SQUARE FEET
#Dependent variable
df['LOG_SALE_PRICE'] = df['SALE PRICE'].map(lambda num: np.log(num))
y = np.matrix(df['LOG_SALE_PRICE']).transpose()
#Independent variables
x = np.matrix(df['GROSS SQUARE FEET']).transpose()
#Appending the constant column
X = sm.add_constant(x)

est2 = sm.OLS(y,X).fit()
print 'Linear Model 2'
print 'Square feet coefficient: ', est2.params[1]
print 'Intercept: ', est2.params[0]
print 'P-Values: ', est2.pvalues
print 'R-Squared: ', est2.rsquared

#visualization
# plt.figure()
# sns.jointplot('GROSS SQUARE FEET', 'SALE PRICE', df, kind = 'reg')
# plt.show()

#Multiple Regression on:
# "SALE PRICE" 
# "GROSS SQUARE FEET"
# "BUILDING CLASS CATEGORY"
df.rename(columns={
				   "SALE PRICE":"sale_price", 
				   "GROSS SQUARE FEET":"gross_square_feet",
				   "BUILDING CLASS CATEGORY":"building_class"
				   }, inplace=True)
est3 = smf.ols(formula = "sale_price ~ C(building_class) + gross_square_feet",
			   data = df).fit()
print 'Regression Model'
print est3.params
print est3.summary()
