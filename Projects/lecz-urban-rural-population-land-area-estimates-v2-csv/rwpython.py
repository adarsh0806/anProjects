import collections
import pprint
population_dict = collections.defaultdict(int)
pop2100_dict = collections.defaultdict(int)
with open('lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
	#skip the header
    header = next(inputFile)
    arealist = []
    for line in inputFile:
    	line = line.rstrip().split(',')
    	#line[5] = Population2010
    	line[5] = float(line[5])
    	#LandArea
    	line[7] = float(line[7])
    	#pop 2100
    	line[6] = int(line[6])
    	if line[1] == 'Total National Population':
    		#key is continent, value is the total population
    		population_dict[line[0]] += line[5]
    		pop2100_dict[line[0]] += line[6]
    		arealist.append(line[7])
    
    print "arealist\n", arealist	
    #calculate the population change between 2010 and 2100
    print "\nPopulation in 2010\n"
    pprint.pprint(population_dict)
    
    print "\nPopulation in 2100\n"
    pprint.pprint(pop2100_dict)
    growthdict = {}
    for k in population_dict:
    	if k in pop2100_dict:
    		growth = int(pop2100_dict[k]) - int(population_dict[k])
    		growthdict[k] = growth
		

    print "\nGrowth of population in various continents: ",growthdict

    # pop_density = {}
    # for k in population_dict:
    # 	pass
    	# for i in arealist:
    	# 	print population_dict[k]
    	#pop_density[k] = population_dict[k]/

with open('national_population2010.csv', 'w') as outputFile:
	outputFile.write('continent, 2010_population\n')
	for key, value in population_dict.iteritems():
		outputFile.write(key + ',' + str(value) + '\n')


