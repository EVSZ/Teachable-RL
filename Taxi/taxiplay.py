import gym
import time
import numpy as np
import random
from IPython.display import clear_output

env = gym.make("Taxi-v3", render_mode="human").env

q_table = np.loadtxt('q_table2', delimiter=',')

total_epochs, total_penalties = 0, 0
episodes = 100
frames = []

for _ in range(episodes):
    state, env_info = env.reset()
    epochs, penalties, reward = 0, 0, 0
    
    terminated = False
    truncated = False
    
    while not terminated or truncated:
        action = np.argmax(q_table[state])
        state, reward, terminated, truncated, info = env.step(action)

        if reward == -10:
            penalties += 1
        
        frames.append({
            'frame': env.render(),
            'state': state,
            'action': action,
            'reward': reward
        })
            
        epochs += 1

    total_penalties += penalties
    total_epochs += epochs

print(f"Results after {episodes} episodes:")
print(f"Average timesteps per episode: {total_epochs / episodes}")
print(f"Average penalties per episode: {total_penalties / episodes}")