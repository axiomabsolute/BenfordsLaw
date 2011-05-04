from __future__ import division
import matplotlib.pyplot as plt
from numpy import linspace
from math import log

def MakeInterval(start=1, end=9, delta=1):
    result = []
    while start < end:
        result.append(start)
        start = start + delta
    return result

def BenfordsLawTable(step=.01):
    result = []
    sample = MakeInterval(delta=step)
    for i in sample:
        row = []
        for j in sample:
            row.append(i*j)
        result.append(row)
    return result

def BenfordsLawDict(step=.01):
    table = BenfordsLawTable(step)
    counts = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for i in table:
        for j in i:
            counts[int(str(j)[0])] += 1
    return counts

def BenfordsLawExample():
    counts = map(BenfordsLawDict, [1,.5,.25,.1,.01])
    for count in counts:
        plt.plot(count.keys(),map(lambda x: x/sum(count.values()),count.values()),'bs')
    plt.show()
	
def BenfordsLawSteps():
	counts = map(BenfordsLawDict, [1,.75,.5,.25,.1,.01])
	samples = linspace(1.0,9.0,250)
	bl = map(lambda s: log(1+(1/s),10),samples)
	
	plt.plot(counts[0].keys(),map(lambda x: x/sum(counts[0].values()),counts[0].values()),'bs')
	plt.plot(samples,bl,linewidth=1.0)
	plt.show()
	plt.plot(counts[1].keys(),map(lambda x: x/sum(counts[1].values()),counts[1].values()),'bs')
	plt.plot(samples,bl,linewidth=1.0)
	plt.show()
	plt.plot(counts[2].keys(),map(lambda x: x/sum(counts[2].values()),counts[2].values()),'bs')
	plt.plot(samples,bl,linewidth=1.0)
	plt.show()
	plt.plot(counts[3].keys(),map(lambda x: x/sum(counts[3].values()),counts[3].values()),'bs')
	plt.plot(samples,bl,linewidth=1.0)
	plt.show()
	plt.plot(counts[4].keys(),map(lambda x: x/sum(counts[4].values()),counts[4].values()),'bs')
	plt.plot(samples,bl,linewidth=1.0)
	plt.show()
	plt.plot(counts[5].keys(),map(lambda x: x/sum(counts[5].values()),counts[5].values()),'bs')
	plt.plot(samples,bl,linewidth=1.0)
	plt.show()