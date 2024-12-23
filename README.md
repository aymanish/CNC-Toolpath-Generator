# CookieCutterCNC: CNC Toolpath Generation Algorithms

This repository contains two algorithms that generate toolpaths for CNC machines: a **zigzag toolpath** for rectangular shapes and a **spiral toolpath** for circular shapes. These algorithms use parametric equations to define the toolpaths in 2D geometry. The toolpaths are animated using `matplotlib` and can be controlled with sliders for various parameters. 

A c++ application using the python testbed is also being developed usign the same concepts. So far only Spiral is working within the c++ build. The goal is to have a working application that lets you create a cnc path mimicking cookie cutting in 2d spaces employing genetic algorithms to allocate the task order and cnc toolpaths to cut the shapes. More complex work with contouring paths and irregular path interpolation in the future.

## Table of Contents
- [Introduction](#introduction)
- [Zigzag Toolpath Algorithm](#zigzag-toolpath-algorithm)
  - [Mathematical Notation](#mathematical-notation)
  - [Code Explanation](#code-explanation)
- [Spiral Toolpath Algorithm](#spiral-toolpath-algorithm)
  - [Mathematical Notation](#mathematical-notation-1)
  - [Code Explanation](#code-explanation-1)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

---

## Introduction

This repository implements two algorithms for generating toolpaths used in CNC (Computer Numerical Control) machining. The algorithms are designed to generate paths for cutting operations, such as milling or engraving, on rectangular and circular areas. The toolpaths are animated to visualize the cutting process based on adjustable parameters.

### Key Features:
- **Zigzag Toolpath**: Fills a rectangular area by alternating between left-to-right and right-to-left rows.
- **Spiral Toolpath**: Fills a circular area using a spiral pattern, starting from the center and moving outward.

Both algorithms are implemented in Python using `numpy` for numerical computation and `matplotlib` for visualization and animation.

---

## Zigzag Toolpath Algorithm

The zigzag toolpath algorithm generates paths for covering a rectangular area. The path alternates directions (left-to-right, right-to-left) for each row, ensuring a continuous zigzag pattern across the area.

### Mathematical Notation

To describe the zigzag path mathematically, we use the following parametric equations for the x and y coordinates:

Let:
- \( w \) be the width of the rectangle
- \( h \) be the height of the rectangle
- \( s \) be the spacing between rows

We define the path as follows:

- The y-coordinate is spaced by \( s \), starting at \( y_0 = 0 \) and continuing until the height \( h \). The y-coordinates are given by:

  \[
  y_i = i \cdot s, \quad i = 0, 1, 2, \dots, \left\lceil \frac{h}{s} \right\rceil
  \]

- The x-coordinate alternates between 0 and \( w \) for each row. For each \( y_i \), the x-coordinates are defined by:

  \[
  x_i = \begin{cases}
    0 \quad \text{if the row number is even} \\
    w \quad \text{if the row number is odd}
  \end{cases}
  \]

This results in a zigzag pattern where the x-coordinate alternates between 0 and the width of the rectangle, and the y-coordinate progresses with the row number.

### Code Explanation

The code for the zigzag toolpath uses the following steps:

1. **Initialization**: Set the initial width, height, and spacing.
2. **Path Computation**: Calculate the x and y coordinates for the zigzag pattern using the parametric equations above.
3. **Animation**: Update the plot dynamically as the sliders for width, height, and spacing are adjusted.
4. **Reset Functionality**: Reset the parameters to their initial values.

```python
def compute_zigzag(width, height, spacing):
    x_values = []
    y_values = []
    direction = 1  # Start left-to-right

    num_rows = int(np.ceil(height / spacing))
    y_coords = np.linspace(0, height, num_rows + 1)

    for y in y_coords:
        if direction == 1:
            x_values.extend([0, width])  # Move left-to-right
        else:
            x_values.extend([width, 0])  # Move right-to-left
        y_values.extend([y, y])
        direction *= -1

    return np.array(x_values), np.array(y_values)
```

---

## Spiral Toolpath Algorithm

The spiral toolpath algorithm generates a path for covering a circular area in a spiral pattern. The spiral starts at the center of the circle and gradually moves outward.

### Mathematical Notation

The spiral is defined using the following parametric equations for the x and y coordinates:

Let:
- \( R \) be the radius of the circle
- \( s \) be the spacing between successive loops
- \( \theta \) be the angular position

The radius \( r(\theta) \) increases linearly with \( \theta \) as:

\[
r(\theta) = k \cdot \theta
\]

where \( k \) is a constant given by:

\[
k = \frac{s}{2\pi}
\]

The parametric equations for the spiral are:

\[
x(\theta) = r(\theta) \cdot \cos(\theta)
\]
\[
y(\theta) = r(\theta) \cdot \sin(\theta)
\]

where \( \theta \) ranges from 0 to \( \theta_{\text{max}} \), with \( \theta_{\text{max}} = \frac{R}{k} \).

### Code Explanation

The code for the spiral toolpath follows these steps:

1. **Initialization**: Set the initial radius, spacing, and angular resolution.
2. **Path Computation**: Calculate the x and y coordinates for the spiral using the parametric equations above.
3. **Animation**: Animate the spiral path as the parameters change.
4. **Reset Functionality**: Reset the parameters to their initial values.

```python
def compute_spiral_and_circle():
    k = s / (2 * np.pi)
    theta_max = R / k
    theta_values = np.arange(0, theta_max, theta_step)
    r_values = k * theta_values
    x_values = r_values * np.cos(theta_values)
    y_values = r_values * np.sin(theta_values)
    
    circle_theta = np.linspace(0, 2 * np.pi, 500)
    circle_x = R * np.cos(circle_theta)
    circle_y = R * np.sin(circle_theta)
```

---

## Installation

To run this code, you need Python and the following libraries:

- `numpy`
- `matplotlib`

You can install the required libraries with pip:

```bash
pip install numpy matplotlib
```

---

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/CNC-Toolpath-Generation.git
    ```

2. Run the script:

    ```bash
    python toolpath_visualization.py
    ```

3. Use the sliders to adjust the parameters and visualize the toolpaths.

4. Click the **Reset** button to reset the parameters to their initial values.

---

