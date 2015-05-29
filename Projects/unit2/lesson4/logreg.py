# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import string
import statsmodels.api as sm
import pylab as py 

'''
What is the probability of getting a loan from the Lending Club 
for $10,000 at an interest rate ≤ 12percent with a FICO score of 750?

'''
#http://blog.yhathq.com/posts/logistic-regression-and-python.html

loansData = pd.read_csv('loansData.csv', nrows = 5)
loansData.dropna(inplace = True)
df = pd.DataFrame(loansData)

ir = df['Interest.Rate']
ll = df['Loan.Length']
fr = df['FICO.Range']
ar = df['Amount.Requested']

clean_ir = ir.map(lambda x: float(x.rstrip('%')))
clean_ll = ll.map(lambda x: x.rstrip(' months'))
fs = [int(i.split('-')[0]) for i in fr]

#Update the dataframe
ir = clean_ir 
ll = clean_ll

#Add the new FICO.Score column to the dataframe
df['FICO.Score'] = fs  

#Add the IR
df['IR_TF'] = (ir < 12).astype(int)
ir_tf = df['IR_TF']

#Add the intercept column
df['Intercept'] = float(1.0)

ind_vars = list(df.columns.values)

new_df = pd.DataFrame(columns = ['Loan_amount', 'FICO_Score', 'Interest_Rate_Bin', 'Intercept'])
new_df['Loan_amount'] = df['Amount.Funded.By.Investors']
new_df['FICO_Score'] = fs
new_df['Interest_Rate_Bin'] = ir_tf
new_df['Intercept'] = 1.0
print new_df
# new_df.hist()
# py.show()
#Define the Logistic Regression model
training_cols = new_df.columns[1:]
logit = sm.Logit(new_df['Loan_amount'], new_df[['FICO_Score','Interest_Rate_Bin','Intercept']])
result = logit.fit()
print result.summary()
