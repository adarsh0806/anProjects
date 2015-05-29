# -*- coding: utf-8 -*-
from scipy import stats
import collections
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import string
import statsmodels.api as sm

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
# ir_tested = [i if i < 12 for i in ir]
# for i in ir:
# 	if i < 12:
# 		df['IR_TF'].append(i)
# irtf = ir.map(lambda x:irtf.append(x), filter(lambda i: if i < 12))

#Add the new columns
df['IR_TF'] = (ir < 12).astype(int)
irtf = df['IR_TF']
ind_vars = list(df.columns.values)
print df

# Interest rate varies with FICO score and the loan amount desired
# logit = sm.Logit(df['IR_TF'], df)
# result = logit.fit()


# def logistic_function(fico_score, loan_amount):
# 	interest_rate = (-1 * 60.125) + (0.087423 * fico_score) − (0.000174 * loan_amount)
# 	p = 100
# 	#p = 1/(1 + e^(intercept + 0.087423(fico_score) − 0.000174(loan_amount))
# 	print "The probability is :", p*100
# 	return p



# '''
# What is the probability of getting a loan from the Lending Club for $10,000 
# at an interest rate ≤ 12 percent with a FICO score of 750?
# '''
# logistic_function(750, 10000)




