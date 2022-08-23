import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = numpy.mean(speed)

print("mean value is ", mean)

percentage = 75
percentile = numpy.percentile(speed, percentage)

print("percentile of ", percentage, " is ", percentile)