import matplotlib.pyplot as plt
import numpy as np

# Phasor data (magnitude and angle in degrees)
phasors = [
    {'magnitude': 3.3, 'angle': np.deg2rad(30), 'color': 'b', 'label': '$\mathbf{V}_1$ (3.3∠30°)'},
    {'magnitude': 5, 'angle': np.deg2rad(225), 'color': 'r', 'label': '$\mathbf{V}_2$ (5∠225°)'}
]

ax = plt.subplot(111, projection='polar')

# Plot each phasor
for phasor in phasors:
    plt.plot([0, phasor['angle']],
            [0, phasor['magnitude']], 
            linewidth=3, 
            color=phasor['color'],
            label=phasor['label'])

    # Add marker at phasor tip
    plt.plot(phasor['angle'],
            phasor['magnitude'], 
            marker='o', 
            markersize=8, 
            color=phasor['color'])

# Values of r (magnitude)
ax.set_yticks(list(range(0, 7, 1)))

# Set r label position
ax.set_rlabel_position(0)

# Grid
plt.grid(True, linestyle='--', alpha=0.7)

# Title and Legend
plt.title('Phasor Diagram', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Save figure
plt.savefig('./bin/img/polar.png', dpi=300, bbox_inches='tight')
