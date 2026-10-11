import numpy as np

dt = 0.1                 # seconds per update
duration = 10.0          # seconds
steps = int(round(duration / dt))

# State order: [east position, north position, east velocity, north velocity]
# Units: [m, m, m/s, m/s]
initial_state = np.array([0.0, 0.0, 30.0, 10.0])

# For constant velocity:
# position_next = position + velocity * dt
# velocity_next = velocity
F = np.array([
    [1.0, 0.0, dt,  0.0],
    [0.0, 1.0, 0.0, dt ],
    [0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 1.0],
])

# Simulate by applying F once per time step.
state = initial_state.copy()
for _ in range(steps):
    state = F @ state

# Independent analytical answer: position = starting position + velocity * time.
expected_position = initial_state[:2] + initial_state[2:] * duration
expected_state = np.concatenate((expected_position, initial_state[2:]))

print("Simulated final state:  ", state)
print("Analytical final state: ", expected_state)