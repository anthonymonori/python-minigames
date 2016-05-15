python-minigames
======================

Mini-games created as part of the Coursera course "An Introduction to Interactive Programming in Python" provided by Rice University, and later converted and modified to work outside of [CodeSkulptor.org](http://www.CodeSkulptor.org) as well.

Tested with Python 2.7!

# How to run
```
git clone https://github.com/anthonymonori/python-minigames.git
cd python-minigames
pip install -U -r requirements.txt
python check.py
python <game-name>.py
```

# Games
### Blackjack
The game requires no Introduction to any of us. Simply 'Hit' or 'Stand' or start a new round by clicking on the 'Deal' button. You bust if you go over `21` and A(ce) can be either `1` or `11`. King, Queen and Jack are valued at `10`. All other cards represent their own value.

![Blackjack screenshot](./screenshots/blackjack.png?raw=true 'Blackjack screenshot')

### Rock, Paper, Scissors, Lizard, Spock
_This game is not compatible with CodeSkulptor.org_

A modified version of the well-known 'Rock, Paper, Scissors' game with the addition of two extra choices: Lizard and Spock (yes, from Star Trek).

In short:

`Scissor > Paper > Rock > Lizard > Spock > Scissor > Lizard > Paper > Spock > Rock > Scissors`

In a bit longer form:

`Scissors cuts Paper covers Rock crushes Lizard poisons Spock smashes Scissors decapitates Lizard eats Paper disproves Spock vaporizes Rock crushed Scissors.`

![RPSLS screenshot](./screenshots/rpsls.png?raw=true 'RPSLS screenshot')

### Stopwatch
Not much to explain: just a simple stopwatch.

![Stopwatch screenshot](./screenshots/stopwatch.png?raw=true 'Stopwatch screenshot')

### Guess the number
A simple game where you have to guess the number between 1-100 or 1-1000 out of 7 tries. Once you try an guess, it will tell you if either you have to select a higher or a lower number, or that you got it right!

![Guess the number screenshot](./screenshots/guessthenumber.png?raw=true 'Guess The Number screenshot')

### Asteroids
A python adaptation of the well-known Asteroids game from Atari. Use the left-right keys to change the angle of the rocket and press the back-forward to throttle.

![Asteroid screenshot](./screenshots/asteroids.png?raw=true 'Asteroid screenshot')

### Memory
A simple and well-known memory game where you have to guess the pair of cards by always folding up 2 of them. Each two-card fold counts as a `move` and you have to unfold them all by the least number of `moves` to win.

![Memory screenshot](./screenshots/memory.png?raw=true 'Memory screenshot')

### Pong
Another well known Atari game adaptation in Python. To move the paddles, use the W-S keys for Player 1 and the arrow keys (up-down) for Player 2. The gameplay never ends, but there's an option to Restart the score.

![Pong screenshot](./screenshots/pong.png?raw=true 'Pong screenshot')

# Problems?
I would prefer if you would open an issue under the `Issues` tab here on GitHub!

# License
Freely provided under the MIT License.
