# Three-Body Simulation

A Python-based interactive simulation of the N-body problem, with a focus on three-body gravitational interactions. This project provides both a PyGame-based interactive visualization and a Manim-based animation system for studying gravitational dynamics between multiple masses in 2D space.

## Overview

The simulation demonstrates the complex behavior of multiple bodies interacting through gravitational forces. It includes:
- Real-time visualization of gravitational interactions
- Trail effects to show the path of each mass
- Interactive controls for simulation parameters
- Support for both interactive PyGame display and Manim animations

## Features

- Interactive simulation with multiple masses
- Gravitational force calculations between all bodies
- Customizable parameters (mass, velocity, position)
- Visual trails showing the path of each mass
- Grid display for reference
- Collision detection and boundary handling
- Two visualization options:
  - Interactive PyGame interface
  - Manim-based animations for high-quality video output

## Requirements

- Python 3.x
- PyGame
- Manim (optional, for animations)
- NumPy

## Project Structure

- `three_body_simulation.py`: Main PyGame simulation interface
- `mass.py`: Class definition for mass objects and their properties
- `system.py`: System class handling physics calculations and mass interactions
- `manim_sim.py`: Manim-based animation system

## Usage

To run the interactive PyGame simulation:
```bash
python three_body_simulation.py
```

For Manim animations:
```bash
python manim_sim.py
```

## Physics Implementation

The simulation implements:
- Newton's law of universal gravitation
- Velocity-based position updates
- Basic collision detection
- Boundary conditions

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for improvements and bug fixes.

## License

This project is open source and available under the MIT License.
