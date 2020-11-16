import numpy as np

class WindyGridworld:
	def __init__(self, grid_size, start, goal, winds, moves, stochastic):
		self.grid_size = grid_size
		self.start = start
		self.goal = goal
		self.winds = winds
		self.moves = moves
		self.stochastic = stochastic		

	def step(self, cur, action):
		wind = self.winds[cur[0]]
		if self.stochastic and wind != 0:
			wind += np.random.randint(-1,2)
		nxt = cur[0] + self.moves[action][0], cur[1] + self.moves[action][1] 
		nxt = nxt[0], nxt[1] + wind
		nxt = min(nxt[0], self.grid_size[0] - 1), min(nxt[1], self.grid_size[1] - 1)
		nxt = max(nxt[0], 0), max(nxt[1], 0)
		reward = -1
		return nxt, reward
