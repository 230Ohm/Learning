import matplotlib
import matplotlib.pyplot as plt

print("Plotting started")
print("Backend:", matplotlib.get_backend())

plt.plot([0, 1, 2], [0, 1, 4])
plt.title("Plot test")

plt.savefig("plot_test.png")
print("Saved plot_test.png")

plt.show()
print("Finished")