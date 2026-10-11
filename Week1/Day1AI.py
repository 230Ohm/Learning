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

# Save the initial state, then every updated state.
state = initial_state.copy()
history = [state.copy()]

for _ in range(steps):
    state = F @ state
    history.append(state.copy())

# Each row contains the state at one time step.
truth = np.array(history)            # Shape: (101, 4)
time = np.arange(steps + 1) * dt      # Times: 0.0 through 10.0 seconds

# Independent analytical answer: position = starting position + velocity * time.
expected_position = initial_state[:2] + initial_state[2:] * duration
expected_state = np.concatenate((expected_position, initial_state[2:]))

# Print only when running Day1.py directly, not when importing it.
if __name__ == "__main__":
    print("Simulated final state:  ", state)
    print("Analytical final state: ", expected_state)
    print("Trajectory shape:      ", truth.shape)