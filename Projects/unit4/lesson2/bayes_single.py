import os
import pandas as pd
import subprocess

#directories with the spam and ham data
#Source: http://www.aueb.gr/users/ion/data/enron-spam/
spamdir = '/Users/adarshnair/Desktop/Thinkful/Projects/unit4/lesson2/enron1/spam'
hamdir = '/Users/adarshnair/Desktop/Thinkful/Projects/unit4/lesson2/enron1/ham'

#spam filter based on the presence of individual words
'''
p(spam) = 1500/(1500+3672)
p(ham) = 1 - p(spam)
p(meeting|spam) = 16/1500
p(meeting|ham) = 153/3672

p(spam|meeting) = p(meeting|spam) * p(spam)/p(meeting)

'''


def spam_prob(word):
	num_spam = float(len([i for i in os.listdir(spamdir)]))
	num_ham = float(len([i for i in os.listdir(hamdir)]))
	#probability of getting a spam email p(spam)
	p_spam = num_spam/(num_spam + num_ham)
	#probability of getting a ham email p(ham) i.e. not spam
	p_ham = 1 - p_spam
	#count the number of occurrances of 'word' (taken in argument) in spam
	#p(word|spam)
	#grep -il meeting enron1/spam/*.txt | wc -l
	cmd1 = 'grep -il ' + word + ' ' + spamdir + '/*.txt'
	word_count_spam = len(subprocess.check_output([cmd1], shell = True).splitlines())
	print "word_count_spam : ", word_count_spam
	#p(meeting|spam)
	p_word_spam = word_count_spam/num_spam
	#probability of finding 'meeting' given we know its spam
	print "p(meeting|spam) : ", p_word_spam

	#count the number of occurrances of 'word' (taken in argument) in ham
	#p(word|ham)
	#grep -il meeting enron1/ham/*.txt | wc -l
	cmd = 'grep -il ' + word + ' ' + 'enron1/ham/*.txt'
	word_count_ham = len(subprocess.check_output([cmd], shell=True).splitlines())
	print "word_count_ham : ", word_count_ham
	# p(meeting|ham)
	p_word_ham = word_count_ham/num_ham
	#probability of finding 'meeting' given we know its ham
	print "p(meeting|ham) : ", p_word_ham

	p_word = p_word_spam*p_spam + p_word_ham*p_ham
	#p(spam|meeting) = p(meeting|spam) * p(spam)/p(meeting)
	#prob of an email being spam, given the word meeting is in it
	final_prob = p_word_spam * (p_spam/p_word)
	print "Probability of an email being spam, given the word meeting is in it: ", final_prob
	return final_prob


spam_prob('meeting')





