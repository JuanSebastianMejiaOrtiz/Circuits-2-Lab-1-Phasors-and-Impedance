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
    ax.plot([0, phasor['angle']],
            [0, phasor['magnitude']], 
            linewidth=3, 
            color=phasor['color'],
            label=phasor['label'])

    # Add marker at phasor tip
    ax.plot(phasor['angle'],
            phasor['magnitude'], 
            marker='o', 
            markersize=8, 
            color=phasor['color'])

# Values of r (magnitude)
ax.set_yticks(list(range(0, 7, 1)))

# Set r label position
ax.set_rlabel_position(0)

# Grid and labels customization
ax.grid(True, linestyle='--', alpha=0.7)

# Legend
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Title
plt.title('Phasor Diagram', pad=20)

# Save figure
plt.savefig('./bin/polar.png', dpi=300, bbox_inches='tight')

# Grid and labels customization
# ax.set_theta_zero_location('E')  # 0° points East
# ax.set_theta_direction(-1)       # Clockwise angle increase
# ax.set_rlabel_position(0)        # Radial labels at 0°
# ax.set_yticks(np.arange(0, 7, 1))  # Radial ticks
# ax.grid(True, linestyle='--', alpha=0.7)
#
# # Title and legend
# plt.title('Phasor Diagram', pad=20)
# ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
#
# # Save figure
# plt.savefig('./bin/polar.png', dpi=300, bbox_inches='tight')
