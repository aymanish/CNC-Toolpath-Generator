import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Initial Parameters
width_init = 6  # Initial width of the rectangle
height_init = 4  # Initial height of the rectangle
spacing_init = 0.5  # Initial spacing of the zigzag

# Global variables for sliders
width = width_init
height = height_init
spacing = spacing_init

# Function to compute zigzag path
def compute_zigzag(width, height, spacing):
    x_values = []
    y_values = []
    direction = 1  # Start left-to-right

    # Compute number of rows based on height and spacing
    num_rows = int(np.ceil(height / spacing))  # Ensure full height is covered
    y_coords = np.linspace(0, height, num_rows + 1)  # Include the top boundary

    for y in y_coords:
        if direction == 1:
            x_values.extend([0, width])  # Move left-to-right
        else:
            x_values.extend([width, 0])  # Move right-to-left
        y_values.extend([y, y])  # Keep y-coordinate constant for the row
        direction *= -1  # Flip direction for next row

    return np.array(x_values), np.array(y_values)

# Compute initial zigzag
x_values, y_values = compute_zigzag(width, height, spacing)

# Visualization
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)  # Leave space for sliders/buttons
ax.set_aspect('equal', adjustable='datalim')
ax.set_xlim(-1, width_init + 1)
ax.set_ylim(-1, height_init + 1)

# Plot elements
zigzag_line, = ax.plot([], [], lw=2, color='blue')
rect_outline, = ax.plot(
    [0, width_init, width_init, 0, 0],
    [0, 0, height_init, height_init, 0],
    color='red', lw=1.5
)

# Function to update the plot
def update_plot(val=None):
    global width, height, spacing, x_values, y_values
    width = slider_width.val
    height = slider_height.val
    spacing = slider_spacing.val

    # Recompute zigzag path
    new_x_values, new_y_values = compute_zigzag(width, height, spacing)

    # Update rectangle outline
    rect_outline.set_data(
        [0, width, width, 0, 0],
        [0, 0, height, height, 0]
    )

    # Directly update zigzag path
    zigzag_line.set_data(new_x_values, new_y_values)

    # Save new values
    x_values[:], y_values[:] = new_x_values, new_y_values

    fig.canvas.draw_idle()  # Ensure the canvas is updated

# Sliders
ax_slider_width = plt.axes([0.2, 0.2, 0.65, 0.03])
slider_width = Slider(ax_slider_width, 'Width', 2, 10, valinit=width_init)

ax_slider_height = plt.axes([0.2, 0.15, 0.65, 0.03])
slider_height = Slider(ax_slider_height, 'Height', 2, 10, valinit=height_init)

ax_slider_spacing = plt.axes([0.2, 0.1, 0.65, 0.03])
slider_spacing = Slider(ax_slider_spacing, 'Spacing', 0.1, 1, valinit=spacing_init)

slider_width.on_changed(update_plot)
slider_height.on_changed(update_plot)
slider_spacing.on_changed(update_plot)

# Reset Button
def reset(event):
    global width, height, spacing
    width = width_init
    height = height_init
    spacing = spacing_init
    slider_width.reset()
    slider_height.reset()
    slider_spacing.reset()
    update_plot()

ax_button_reset = plt.axes([0.8, 0.025, 0.1, 0.04])
button_reset = Button(ax_button_reset, 'Reset')
button_reset.on_clicked(reset)

# Initial plot rendering
update_plot()

plt.title("Animated Zigzag Toolpath with Sliders")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
