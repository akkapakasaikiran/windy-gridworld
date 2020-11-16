# windy-gridworld

A simple python implementation of the Windy Gridworld problem from [1] intended to serve pedagogical purposes.

## Details
* Run `python3 main.py` to generate plots for the below mentioned tasks. It supports a few comand line arguments too. 
* Task 1: Example 6.5: An <img src="https://render.githubusercontent.com/render/math?math=\epsilon">-greedy SARSA agent with movement allowed in four directions.
* Task 2: Exercise 6.9: Now the agent can move in eight directions.
* Task 3: Exercise 6.10: Now the wind isn't deterministic.
* Task 4: A comparison of Q-learning, SARSA, and Expected SARSA for this problem.
* The file `environment.py` helps modularize the code for returning rewards and next states for the actions taken by the agent.
* The file `agent.py` has the learning algorithms along with methods to manage agent data.


## References
* [1] Sutton and Barto, Reinforcement Learning: An Introduction, http://incompleteideas.net/book/RLbook2020.pdf, pg 130