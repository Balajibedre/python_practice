import matplotlib.pyplot as pyplot
import numpy as np

data = np.array([50,20,10,15,5])
labels = ['Python','JavaScripts','C#','Java','PHP']

pyplot.pie(data, labels = labels, shadow = True)
pyplot.show()