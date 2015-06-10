import cProfile
import unittest
#cProfile.runctx('Your code here', globals(), locals(), 'output_file')
class Test(unittest.TestCase):
	def testSomething(self):
		self.DoSomethingIDontCareAbout()
		param = 'whatever'
		self.RunFunctionIThinkIsSlow(param)
		self.AssertSomeStuff()


 
########################## AFTER PROFILING ##########################
import unittest
import cProfile

class Test(unittest.TestCase):
	def testSomething(self):
		self.DoSomethingIDontCareAbout()
		param = 'whatever'
		cProfile.runctx(
			'self.RunFunctionIThinkIsSlow(param)',
			globals(),
			locals(),
			'myProfilingFile.pstats')
		self.AssertSomeStuff()

#CONVERTING A PSTATS FILE TO A GRAPH
''''
python gprof2dot -f pstats myProfileFile | dot -Tpng -o image_output.png
'''