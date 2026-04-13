import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 data points between 0 and 10
x = np.linspace(0, 10, 1000)
# Calculate the sine wave for those points
y = np.sin(x)

# Create the visual plot
plt.figure(figsize=(8, 4))
plt.plot(x, y, color='cyan', linewidth=2)
plt.title("System Verification: Sine Wave")
plt.grid(True, linestyle='--', alpha=0.6)

# Display the render
plt.show()