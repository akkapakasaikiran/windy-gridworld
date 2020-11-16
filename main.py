from environment import WindyGridworld
from agent import Agent
import matplotlib.pyplot as plt
import numpy as np
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--alpha', help='Learning rate', default='0.5', type=float)
parser.add_argument('--epsilon', help='Exploration rate', default='0.1', type=float)
parser.add_argument('--num_episodes', help='Number of episodes to spend learning', default=200, type=int)
parser.add_argument('--num_seeds', help='Number of seeds to average over', default=20, type=int)
args = parser.parse_args()

alpha = args.alpha
epsilon = args.epsilon
num_episodes = args.num_episodes
num_seeds = args.num_seeds


# E, N, W, S 
standard_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# E, NE, N, NW, W, SW, S, SE
kings_moves = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

env_config = {
	'grid_size': (10, 7),
	'start': (0, 3),
	'goal': (7, 3),
	'winds': [0, 0, 0, 1, 1, 1, 2, 2, 1, 0],
	'moves': standard_moves,
	'stochastic': False,
}

agent_config = {
	'alpha': alpha,
	'epsilon': epsilon,
	'start': env_config['start'],
	'goal': env_config['goal'],
	'grid_size': env_config['grid_size'],
	'num_actions': len(env_config['moves']),
}


def get_plot(algo, title, fresh=True):
	env = WindyGridworld(**env_config)
	
	avg_steps = np.zeros(num_episodes)
	for seed in range(num_seeds):		
		agent = Agent(**agent_config)
		steps = np.array([agent.run_episode(env, algo) for i in range(num_episodes)])
		steps = np.cumsum(steps)
		avg_steps += steps

	avg_steps = avg_steps / num_seeds

	if fresh:
		plt.figure()
		plt.xlabel('No. of time steps')
		plt.ylabel('No. of episodes')
		plt.title(title)
	plt.plot(avg_steps, np.arange(1, num_episodes+1), label=algo)


get_plot('Sarsa', 'Baseline Comparison of different algorithms')
get_plot('Expected Sarsa', 'Baseline Comparison of different algorithms', fresh=False)
get_plot('Q-learning', 'Baseline Comparison of different algorithms', fresh=False)
plt.legend()
plt.savefig('diff_algos.png')


get_plot('Sarsa', 'Standard Moves with non-stochastic wind')
plt.savefig('standard_moves.png')


env_config['moves'] = kings_moves
agent_config['num_actions'] = len(env_config['moves'])
get_plot('Sarsa', 'Kings\' Moves with non-stochastic wind')
plt.savefig('kings_moves.png')


env_config['stochastic'] = True
get_plot('Sarsa', 'Kings\' Moves with stochastic wind')
plt.savefig('stochastic_wind.png')


