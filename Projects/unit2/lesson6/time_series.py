'''
 Time series can be broken into three components so that Y=m+s+e,
  where 
  "Y" is the series, 
  "m" is the trend, 
  "s" is the seasonal component and 
  "e" is random noise. 
 Y=m+s+e

"Exponential smoothing" 
The idea behind this method is to forecast predictions based on a weighted average of 
the most recent observations.
The weighting is typically a geometrically declining series that sums to 1, 
so the most recent observations are given the most weight. 
The result is a smoothed series that reflects the pattern of the most recent observations.

"Auto-Regressive Integrated Moving Average"
A series can be expressed as a function of its most recent observations 
("auto-regressive" indicates a regression of an observation on itself, or more specifically,
running a regression on an observation using previous observations as explanatory variables) 
as well as a trend component of the forecast errors (moving average).

https://www.youtube.com/watch?v=Y2khrpVo6qI

'''
import pandas as pd
import statsmodels.api 
import matplotlib.pyplot as plt

df = pd.read_csv('loanstats2015.csv', nrows = 5, skiprows = 1, low_memory = False)
#converting string to datetime
#create a monthly time series of the loan counts by the issue date
df['issue_d_format'] = pd.to_datetime(df['issue_d']) 
df_time_series = df.set_index('issue_d_format')
year_month_summary = df_time_series.groupby(lambda x: x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']
print loan_count_summary

#ACF
statsmodels.api.graphics.tsa.plot_acf(loan_count_summary)
#PACF
statsmodels.api.graphics.tsa.plot_pacf(loan_count_summary)
