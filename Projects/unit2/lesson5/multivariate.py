import pandas as pd
import statsmodels.api as sm
import numpy as np

loansdata = pd.read_csv('loanstats2015.csv', nrows = 5, skiprows = 1)
df = pd.DataFrame(loansdata)
ir = df['int_rate']
ai = df['annual_inc']
ho = df['home_ownership']
'''
Use income (annual_inc) to model interest rates (int_rate).
Add home ownership (home_ownership) to the model.
Does that affect the significance of the coefficients in the original model? + 
Try to add the interaction of home ownership and incomes as a term.
How does this impact the new model?
'''
#Data cleaning
#Remove % from int_rate
clean_ir = ir.map(lambda x: float(x.rstrip('%')))
clean_ai = ai.map(lambda x: float(x))
clean_ho = ho.map(lambda x: 5 if x == 'RENT' else 10)
ir = clean_ir
ai = clean_ai
ho = clean_ho

#Create new dataframe with annual_inc,int_rate,home_ownership for analysis
new_df = pd.DataFrame(columns = ['Home_Ownership','Interest_Rate','Annual_Income'])
new_df['Home_Ownership'] = ho
new_df['Interest_Rate'] = ir
new_df['Annual_Income'] = ai
#Add intercept column
new_df['Intercept'] = float(1.0)
print new_df
#Model with annual income to model interest rates
model_ai = sm.OLS(new_df['Interest_Rate'], new_df[['Intercept','Annual_Income']])
r1 = model_ai.fit()
print "\nModel of Interest_Rate to Annual_Income: \n",r1.summary()
print "\n\n"
#Model with home ownership to model interest rates
model_ho = sm.OLS(new_df['Interest_Rate'], new_df[['Intercept','Annual_Income','Home_Ownership']])
r2 = model_ho.fit()
print "\nModel of Interest_Rate to Home_Ownership and Annual_Income: \n",r2.summary()


