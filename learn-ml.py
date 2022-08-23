import numpy
import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = numpy.mean(speed)
print("mean value is ", mean)

percentage = 75
percentile = numpy.percentile(speed, percentage)
print("percentile of ", percentage, " is ", percentile)

randomValueArray = numpy.random.uniform(0.0, 5.0, 50)
print("generate an array with random values", randomValueArray)

plt.hist(randomValueArray, 5)
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()