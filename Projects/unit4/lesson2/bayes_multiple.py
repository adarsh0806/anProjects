# -*- coding: utf-8 -*-
# The model’s output is the probability that we’d see a given word vector given that 
# we know it’s spam (or that it’s ham)
# The email vector to be and the various entries are xj, where the j indexes the word
# we can denote “is spam” by c, and we have the following model for p(x|c) 
# i.e., the probability that the email’s vector looks like this considering it’s spam
import os
import pandas as pd
import subprocess
import numpy as np

#directories with the spam and ham data
#Source: http://www.aueb.gr/users/ion/data/enron-spam/
spamdir = '/Users/adarshnair/Desktop/Thinkful/Projects/unit4/lesson2/enron1/spam'
hamdir = '/Users/adarshnair/Desktop/Thinkful/Projects/unit4/lesson2/enron1/ham'

#same logic as in bayes_single.py
def spam_prob(word):
	num_spam = float(len([i for i in os.listdir(spamdir)]))
	num_ham = float(len([i for i in os.listdir(hamdir)]))
	
	#probability of getting a spam email p(spam)
	p_spam = num_spam/(num_spam + num_ham)
	#probability of getting a ham email p(ham) i.e. not spam
	p_ham = 1 - p_spam
	
	#count occurences of 'word' in the spam emails
	cmd1 = 'grep -il ' + word + ' ' + spamdir + '/*.txt | wc -l'
	spam_word_count = float(subprocess.check_output([cmd1], shell = True))
	
	#count occurences of 'word' in the ham emails
	cmd2 = 'grep -il ' + word + ' ' + 'enron1/ham/*.txt | wc -l'
	ham_word_count = float(subprocess.check_output([cmd2], shell = True))
	
	# p(meeting|ham)
	#probability of finding 'meeting' given we know its ham
	p_word_ham = ham_word_count/num_ham
	#print "p(meeting|ham) : ", p_word_ham
	
	#p(meeting|spam)
	p_word_spam = spam_word_count/num_spam
	
	#probability of finding the 'word' using Bayes
	p_word = p_word_spam*p_spam + p_word_ham*p_ham
	
	#p(spam|meeting) = p(meeting|spam) * p(spam)/p(meeting)
	#prob of an email being spam, given the word meeting is in it
	final_prob = p_word_spam * (p_spam/p_word)
	return final_prob

	

#generating a list of all the words in files in the spam dir
#that are longer than 3 alphabets
words = []
for i in os.listdir(spamdir):
	with open(spamdir + '/' + i, 'r') as filename:
		wordlist = [word for word in filename.read().split(' ')
						if word.isalpha() and len(word) > 3 and word not in words]
		words += wordlist


#putting the wordlist data into a dataframe
df = pd.DataFrame(words, columns = ['word'])

#θ is the probability that an individual word is present in 
#a spam email, that is p(word|spam)
#ERROR HERE
df['theta'] = 0
df['wj'] = 0
for word in df['word'].values:
	theta = spam_prob('meeting')
	df['theta'] = theta
	df['wj'] = np.log(theta/1-theta)
print "df['theta'] :\n",df['theta']
print "df['wj']: \n", df['wj']
