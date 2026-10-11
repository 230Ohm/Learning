# final answer should be [300,100,30,10]
import numpy as np
state = np.array([0.0, 0.0, 30.0, 10.0])
F = np.array([
    [1.0, 0.0, 0.1, 0.0],
    [0.0, 1.0, 0.0, 0.1],
    [0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 1.0]
]) # 0.1 here is delta time 
for _ in range(100):
    state = F @ state
print(state)