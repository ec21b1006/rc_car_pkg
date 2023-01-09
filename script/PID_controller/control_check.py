from controller import *
import numpy as np
import matplotlib.pyplot as plt
Car = Controller()
Car.setConst([0.0026,0.0015,0.0015,0.0001])
inputs=[20]
outputs=[]
target=0
Car.setTargetValue(target)
timesteps = np.linspace(0,100,500)
for i in timesteps:
    Car.setCurrentValue(inputs[-1])
    clock.sleep(0.000001)
    output = Car.UpdateOutput()
    inputs.append(output)
    outputs.append(output)
inputs.pop()
plt.plot(timesteps,inputs)
plt.show()