import numpy as np

def _random_argmax(arr):
	return np.random.choice(np.flatnonzero(arr == arr.max()))

class Agent:
	def __init__(self, alpha, epsilon, start, goal, grid_size, num_actions):
		self.alpha = alpha
		self.epsilon = epsilon
		self.grid_size = grid_size
		self.start = start
		self.goal = goal
		self.num_actions = num_actions
		self.Q = np.zeros((self.grid_size[0]*self.grid_size[1], self.num_actions))

	def reset(self):
		self.Q = np.zeros((self.grid_size[0]*self.grid_size[1], self.num_actions))

	def _get_action_dist(self, state):
		action_dist = np.full(self.num_actions, self.epsilon/self.num_actions)
		action_value = self._get_Q(state)
		bool_arr = (action_value == action_value.max())
		num_optimal_actions = action_value[bool_arr].size
		action_dist[np.flatnonzero(bool_arr)] += (1 - self.epsilon) / num_optimal_actions
		return action_dist

	def _choose_action(self, state):
		if np.random.rand() < self.epsilon:
			return np.random.randint(self.num_actions)
		else:
			return _random_argmax(self._get_Q(state))	

	def _get_Q(self, state, action=None):
		if action is None:
			return self.Q[state[0] + self.grid_size[0]*state[1]]
		else:
			return self.Q[state[0] + self.grid_size[0]*state[1], action]

	def _set_Q(self, state, action, val):
		self.Q[state[0] + self.grid_size[0]*state[1], action] = val

	def _sarsa_target(self, reward, nxt, nxt_action):
		return reward + self._get_Q(nxt, nxt_action)

	def _expected_sarsa_target(self, reward, nxt):
		action_dist = self._get_action_dist(nxt)
		return reward + np.sum(action_dist * self._get_Q(nxt))

	def _q_learning_target(self, reward, nxt):
		return reward + np.max(self._get_Q(nxt))

	def _get_target(self, algo, reward, nxt, nxt_action):
		if algo == 'Sarsa':
			return self._sarsa_target(reward, nxt, nxt_action)
		elif algo == 'Expected Sarsa':
			return self._expected_sarsa_target(reward, nxt)
		elif algo == 'Q-learning':
			return self._q_learning_target(reward, nxt)
		else:
			print('Algorithm not implemented')

	def run_episode(self, env, algo):
		steps = 0
		cur = self.start
		action = self._choose_action(cur)
		while cur != self.goal:
			nxt, reward = env.step(cur, action)
			nxt_action = self._choose_action(nxt)

			target = self._get_target(algo, reward, nxt, nxt_action)
			old_val = self._get_Q(cur, action)
			self._set_Q(cur, action, old_val + self.alpha * (target - old_val))

			cur, action = nxt, nxt_action
			steps += 1

		return steps
