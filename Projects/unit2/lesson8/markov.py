import pandas as pd
#https://www.youtube.com/watch?v=uvYTGEZQTEs
df = pd.DataFrame({'rainy': [.4, .7], 
                   'sunny': [.6, .3]
                  }, 
                  index=["rainy", "sunny"])
#print df
#for two transitions
#the chance of it raining two steps (or transitions) after it was sunny is .49
#print df.dot(df)

df1 = pd.DataFrame({'bull': [.9, .15, .25],
					'bear': [.075, .8, .25],
					'stagnant': [.025, .05, .5]},
					index = ['bull','bear','stagnant'])
print df1
times2 = df1.dot(df1)
times3 = times2.dot(df1)
times4 = times3.dot(df1)
times5 = times4.dot(df1)

print times2
print times3
print times4
print times5
