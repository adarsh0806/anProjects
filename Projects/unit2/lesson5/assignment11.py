#http://nbviewer.ipython.org/urls/s3.amazonaws.com/datarobotblog/notebooks/multiple_regression_in_python.ipynb#appendix
import pandas as pd
import statsmodels.formula.api as smf
from IPython.core.display import HTML
def short_summary(est):
    return HTML(est.summary().tables[1].as_html())


df = pd.read_csv('http://statweb.stanford.edu/~tibs/ElemStatLearn/datasets/SAheart.data', index_col=0)
# copy data and separate predictors and response
X = df.copy()
y = X.pop('chd')
#print df.head()
# compute percentage of chronic heart disease for famhist
print y.groupby(X.famhist).mean()
# encode df.famhist as a numeric via pd.Factor
df['famhist_ord'] = pd.Categorical(df.famhist).codes
#est = smf.ols(formula="chd ~ famhist_ord", data=df).fit(
# fit OLS on categorical variables children and occupation
#"dummy-encoding" which encodes a k-level categorical variable into k-1 binary variables.
# In statsmodels this is done using the C() function.
est = smf.ols(formula='chd ~ C(famhist)', data=df).fit()
short_summary(est)

