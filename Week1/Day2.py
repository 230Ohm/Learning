from pathlib import Path
import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import numpy as np
from Day1AI import truth

true_positions = truth[:, :2]

rng = np.random.default_rng(2028)
noise = rng.normal(
    loc=0.0,
    scale=5.0,
    size=true_positions.shape
)
measurements = true_positions + noise

print("Creating figure...", flush=True)

fig, ax = plt.subplots()

ax.plot(
    true_positions[:, 0],
    true_positions[:, 1],
    label="True trajectory"
)
ax.scatter(
    measurements[:, 0],
    measurements[:, 1],
    s=15,
    alpha=0.5,
    label="Noisy measurements"
)

ax.set_xlabel("East position (m)")
ax.set_ylabel("North position (m)")
ax.set_title("True trajectory vs. sensor measurements")
ax.set_aspect("equal", adjustable="box")
ax.grid(True)
ax.legend()
fig.tight_layout()

# Save beside this script so the image is easy to locate.
output = Path(__file__).resolve().with_name("day2_plot.png")
fig.savefig(output, dpi=150)
print("Saved:", output, flush=True)

plt.show(block=True)