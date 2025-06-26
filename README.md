# VW DIGITAL:HUB Backend Technical Test - Elías Esteve Bernal



## 📝 Challenge
For the pilot test of our cleaning robot, we have selected a rectangular factory floor that is currently vacant and free of
obstacles. This floor will provide an ideal testing ground for our robot, allowing us to evaluate its capabilities in a controlled
environment.

The robot will be tasked with cleaning the entire floor, including hard-to-reach corners and crevices. We believe that this test will
demonstrate the effectiveness of our robot's cleaning mechanism, as well as its ability to navigate around obstacles and operate
autonomously. With this successful pilot test, we will be one step closer to launching our cleaning robot into the market, and
providing an innovative solution to the challenges of industrial cleaning.

Here you can see the floor that the robot will be cleaning. As you can see, it's quite dirty:
A cleaning robot's position and orientation is represented by its X and Y coordinates and a letter representing one of the four
cardinal compass points (N, E, S, W). The workspace where the robot operates is divided up into a grid to simplify navigation. For
instance, an example position of the robot could be 0, 0, N, which indicates that the robot is at the bottom-left corner and facing
North.

The robot cleaner at 0,0, N:
To control the robot, the Maintenance Department sends a string of instructions consisting of the letters "L", "R", and "M". The
letter "L" makes the robot spin 90 degrees left, "R" makes it spin 90 degrees right, and "M" tells it to move forward one grid point
in the same direction it is facing.

It is important to note that the square directly North of (X, Y) is (X, Y + 1).

The input for the robot control consists of two lines. The first line is the upper-right coordinates of the workspace, with the bottom
left coordinates assumed to be 0, 0. The second line provides information on the robots deployed. Each robot is represented by
two lines. The first line specifies its position, while the second line is a series of instructions telling the robot how to explore the
workspace.

Each robot operates sequentially, meaning that the second robot will start moving only after the first one has finished.
The output should provide the final coordinates and orientation of each robot.

## 🔍 Interpretations
- The board dimensions (Width and Height) and the robot's position coordinates must have the same number of digits.
- If a robot encounters a wall, it will not advance beyond the board boundary.
- The robots cannot collide with each other
- The input will be a text file.

## 🧠 Architecture

The solution follows:
- **Domain-Driven Design (DDD)** principles
- **Hexagonal architecture**

**Layers:**
```
src/
  domain/          # Entities, Value Objects, Domain exceptions
  application/     # Use cases
  infrastructure/  # Input parser, CLI interface, repositories
  tests/           # Unit and integration tests
```
## 🔄 Input Format

```
WidthHeight
XY DIRECTION
INSTRUCTIONS
```
**Example:**
```
55
12 N
LMLMLMLMM
33 E
MMRMMRMRRM
```
---

## 🚀 Run the Application

### 🔧 1. Set up environment
```bash
python -m venv .venv
source .venv/bin/activate  # (Linux/Mac)
.venv\Scripts\activate     # (Windows)
pip install -r requirements.txt
```

### 🔧 2. Run the CLI
```bash
python -m main < input.txt
```

---

## 🧪 Run Tests
Use `pytest` to run all tests:
```bash
python -m pytest
```


