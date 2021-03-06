# GameOfLife

The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.

[Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

## How to run

```bash
pip install -r requirements.txt
python run.py
```

## How to test

```bash
pip install -r requirements.txt
pytest test
```

## Examples

### 1. The R-pentomino

* Starting shape:

![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Game_of_life_fpento.svg/82px-Game_of_life_fpento.svg.png)

* Simulation:

![](./emulations/r_pentomino.gif)

---

### 2. Oscliator

* Starting shape:

![](./emulations/oscilator.png)

* Simulation:

![](./emulations/oscliator.gif)

---

### 3. Glider

* Starting shape:

![](./emulations/glider.png)

* Simulation:

![](./emulations/glider.gif)

---

### 4. Diehard

* Starting shape:

![](./emulations/diehard.png)

* Simulation:

![](./emulations/diehard.gif)

---

### 5. Spaceship

* Starting shape:

![](./emulations/spaceship.png)

* Simulation:

![](./emulations/spaceship.gif)