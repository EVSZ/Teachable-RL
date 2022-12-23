import gym
import time
import numpy as np
import random
from IPython.display import clear_output

env = gym.make("LunarLander-v2", render_mode="ansi").env
env.reset(seed=69)

q_table = np.zeros([env.observation_space.n, env.action_space.n])

# Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.1

# Plotting metrics
all_epochs = []
all_penalties = []


for i in range(1, 100001):
    state, env_info = env.reset()
    epochs, penalties, reward = 0, 0, 0
    terminated = False
    truncated = False
    
    while not terminated or truncated:
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample() # Explore action space
        else:
            action = np.argmax(q_table[state])
            
        next_state, reward, terminated, truncated, info = env.step(action)
        
        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])
        
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state,action] = new_value
        
        if reward == -10:
            penalties += 1
        
        state = next_state
        epochs += 1
        
    if i % 100 == 0:
        clear_output(wait=True)
        print(f'Episode: {i}')

print("Training finished \n")

np.savetxt('q_table-Moon', q_table, delimiter=',')

print("q_table saved as q_table-Moon \n")

# env = gym.make("Taxi-v3", render_mode="human").env
# env.reset(seed=69)

# q_table = np.loadtxt('q_table', delimiter=',')

# total_epochs, total_penalties = 0, 0
# episodes = 100
# frames = []

# for _ in range(episodes):
#     state, env_info = env.reset()
#     epochs, penalties, reward = 0, 0, 0
    
#     terminated = False
#     truncated = False
    
#     while not terminated or truncated:
#         action = np.argmax(q_table[state])
#         state, reward, terminated, truncated, info = env.step(action)

#         if reward == -10:
#             penalties += 1
        
#         frames.append({
#             'frame': env.render(),
#             'state': state,
#             'action': action,
#             'reward': reward
#         })
            
#         epochs += 1

#     total_penalties += penalties
#     total_epochs += epochs

# print(f"Results after {episodes} episodes:")
# print(f"Average timesteps per episode: {total_epochs / episodes}")
# print(f"Average penalties per episode: {total_penalties / episodes}")