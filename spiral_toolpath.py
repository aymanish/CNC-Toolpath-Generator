import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

# Initial Parameters
R_init = 3  # Radius of the circle
s_init = 0.2  # Spacing between loops
theta_step_init = 0.1  # Angular resolution

# Global variables for sliders
R = R_init
s = s_init
theta_step = theta_step_init

# Fixed number of frames for animation
animation_frames = 500

# Function to compute spiral and circle
def compute_spiral_and_circle():
    global theta_values, r_values, x_values, y_values, circle_x, circle_y
    k = s / (2 * np.pi)
    theta_max = R / k
    theta_values = np.arange(0, theta_max, theta_step)
    r_values = k * theta_values
    x_values = r_values * np.cos(theta_values)
    y_values = r_values * np.sin(theta_values)
    
    # Generate high-resolution circle points
    circle_theta = np.linspace(0, 2 * np.pi, 500)
    circle_x = R * np.cos(circle_theta)
    circle_y = R * np.sin(circle_theta)

compute_spiral_and_circle()

# Visualization
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)  # Adjust space for sliders/buttons
ax.set_aspect('equal', adjustable='datalim')
ax.set_xlim(-R_init - 1, R_init + 1)
ax.set_ylim(-R_init - 1, R_init + 1)

spiral_line, = ax.plot([], [], lw=2, color='blue')
circle_line, = ax.plot(circle_x, circle_y, color='red', lw=1.5)

# Animation function
def update(frame):
    idx = int((frame / animation_frames) * len(theta_values))  # Map frame to theta index
    spiral_line.set_data(x_values[:idx], y_values[:idx])
    return spiral_line,

# Function to reset the plot
def reset(event):
    global R, s, theta_step
    R = R_init
    s = s_init
    theta_step = theta_step_init
    slider_R.reset()
    slider_s.reset()
    slider_theta_step.reset()
    update_plot()

# Function to update plot based on slider values
def update_plot(val=None):
    global R, s, theta_step
    R = slider_R.val
    s = slider_s.val
    theta_step = slider_theta_step.val
    compute_spiral_and_circle()
    ax.set_xlim(-R - 1, R + 1)
    ax.set_ylim(-R - 1, R + 1)
    spiral_line.set_data([], [])
    circle_line.set_data(circle_x, circle_y)

# Sliders
ax_slider_R = plt.axes([0.2, 0.2, 0.65, 0.03])
slider_R = Slider(ax_slider_R, 'Radius (R)', 1, 10, valinit=R_init)

ax_slider_s = plt.axes([0.2, 0.15, 0.65, 0.03])
slider_s = Slider(ax_slider_s, 'Spacing (s)', 0.05, 1, valinit=s_init)

ax_slider_theta_step = plt.axes([0.2, 0.1, 0.65, 0.03])
slider_theta_step = Slider(ax_slider_theta_step, 'Theta Step', 0.01, 1.0, valinit=theta_step_init)

slider_R.on_changed(update_plot)
slider_s.on_changed(update_plot)
slider_theta_step.on_changed(update_plot)

# Reset Button
ax_button_reset = plt.axes([0.8, 0.025, 0.1, 0.04])
button_reset = Button(ax_button_reset, 'Reset')
button_reset.on_clicked(reset)

# Animate
ani = animation.FuncAnimation(fig, update, frames=animation_frames, interval=20, blit=True)

plt.title("Spiral Toolpath Animation with Controls")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
