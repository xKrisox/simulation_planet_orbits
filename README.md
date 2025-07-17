# Planet Simulation

This Python project uses Pygame to visualize a simplified gravitational simulation of the Solar System. It includes the Sun and eight planets, with support for an optional moon orbiting a planet. You can zoom in and toggle trails to observe orbital paths.

## Features

* **Newtonian gravity**: Bodies attract each other according to Newton's law of universal gravitation.
* **Pygame rendering**: Real-time 2D visualization with adjustable zoom levels.
* **Orbital trails**: Toggleable trails showing the recent path of each body.
* **Moon support**: Each planet can have a single moon with its own orbital dynamics.

## Requirements

* Python 3.7+
* Pygame

Install dependencies with:

```bash
pip install pygame
```

## Usage

1. Clone the repository or download `simulation.py`.
2. Install Pygame if not already installed.
3. Run the simulation:

   ```bash
   python simulation.py
   ```
4. Controls:

   * **Z**: Toggle zoom mode (closer view).
   * **Close window**: Exit the simulation.

## Code Overview

* **Constants**:

  * `G`: Gravitational constant.
  * `SCALE`: Conversion factor from meters to pixels for standard view.
  * `ZOOM_SCALE`: Conversion factor for zoomed-in view.
  * `DT`: Time step in seconds (default 1 day).

* **Class `Body`**:

  * Represents a celestial object (planet or moon).
  * **Attributes**: position (`x`, `y`), velocity (`vx`, `vy`), mass, draw radius, color. Moon-specific attributes: `x_moon`, `y_moon`, `vx_moon`, `vy_moon`, `moon_mass`, `moon_radius`, `color_moon`, `number_of_moons`.
  * **Methods**:

    * `update_position(bodies)`: Compute net gravitational forces from other bodies and update positions and velocities.
    * `draw(screen, scale, offset_x, offset_y)`: Render the body (and moon, if present) and its trail.

* **Main Loop**:

  1. Handle events: quit and zoom toggle.
  2. Compute `scale` and camera offsets to keep the Sun centered.
  3. Update and draw all bodies.
  4. Cap the frame rate at 60 FPS.

## Customization

* **Adding bodies**: Create additional `Body` instances and add them to the `bodies` list.
* **Moon orbits**: Set `number_of_moons=1` and provide moon parameters when instantiating a `Body`.
* **Scale & time step**: Adjust `SCALE`, `ZOOM_SCALE`, and `DT` to change visualization scale and simulation speed.

## License

This project is released under the MIT License. Feel free to use and modify.
