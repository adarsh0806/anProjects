'''
Here’s an overview of the process:

Decide on your similarity or distance metric.

Split the original labeled dataset into training and test data.

Pick an evaluation metric. (Misclassification rate is a good one. We’ll explain this more in a bit.)
- precision = (number of true positives)/(number of true positives + number of false positives)
- sensitivity and specificity:
  where sensitivity is here defined as the probability of correctly diagnosing an ill patient as ill; 
  specificity is here defined as the probability of correctly diagnosing a well patient as well.
- accuracy = ratio of the number of correct labels to the total number of labels
- misclassification rate, which is just 1–accuracy. 
  Minimizing the misclassification rate then just amounts to maximizing accuracy

Run k-NN a few times, changing k and checking the evaluation measure.

Optimize k by picking the one with the best evaluation measure.

Once you’ve chosen k, use the same training set and now create a new test set with the people’s ages and incomes that you have no labels for, and want to predict. In this case, your new test set only has one lonely row, for the 57-year-old.
'''
import numpy as np 
import pandas as pd
from sklearn.cross_validation import train_test_split

df = pd.read_csv('SampleData.csv')
'''
df.head()
  age income credit
1  69      3    low
2  66     57    low
3  49     79    low
4  49     17    low
5  58     26   high
6  44     71   high
'''
#save some clean data from the overall data for the testing phase,save randomly selected data, let’s say 20%.
dfTrain, dfTest = train_test_split(df, test_size = 0.2)
#subset of labels for the training set
cl = dfTrain[:,2]
#subset of labels for the test set
true_labels = dfTest[:,2]

