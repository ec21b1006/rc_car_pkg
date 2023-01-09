from controller import *
from math import sin
import matplotlib.pyplot as plt
import numpy as np
#Time is imported as clock
Car = Controller()
Car.setConst([0.1,0.02,0.1,0.05])
Car.setTargetValue(0)
outputs=[]
inputs=list(np.linspace(0,50,500))
targets=list(map(sin,inputs))
for i in inputs:
    Car.setCurrentValue(sin(i))
    output = Car.UpdateOutput()
    outputs.append(output)
plt.plot(inputs,targets)
plt.plot(inputs,outputs)
plt.show()