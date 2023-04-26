import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#makedata
np.random.seed(3)
x= 4 + np.random.normal(0, 2, 24)
y= 4 + np.random.normal(0, 2, len(x))
#size
sizes =np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))
