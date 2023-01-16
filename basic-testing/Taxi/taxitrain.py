import gym
import time
import numpy as np
import random
from IPython.display import clear_output
import matplotlib.pyplot as plt

env = gym.make("Taxi-v3", render_mode="ansi").env

q_table = np.zeros([env.observation_space.n, env.action_space.n])

# Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.1

# Plotting metrics
all_epochs = []
all_penalties = []
all_rewards = []

for i in range(1, 1001):
    state, env_info = env.reset()
    epochs, penalties, reward = 0, 0, 0
    terminated = False
    truncated = False

    while not terminated or truncated:
        # if random.uniform(0, 1) < epsilon:
        #     action = env.action_space.sample()  # Explore action space
        # else:
        #     action = np.argmax(q_table[state])

        # Choose the action with the highest value in the current state
        if np.max(q_table[state]) > 0:
            action = np.argmax(q_table[state])

        # If there's no best action (only zeros), take a random one
        else:
            action = env.action_space.sample()

        next_state, reward, terminated, truncated, info = env.step(action)

        # old_value = q_table[state, action]
        # next_max = np.max(q_table[next_state])

        # new_value = (1 - alpha) * old_value + alpha * \
        #     (reward + gamma * next_max)
        # q_table[state, action] = new_value

        q_table[state, action] = q_table[state, action] + \
            alpha * (reward + gamma *
                     np.max(q_table[next_state]) - q_table[state, action])

        if reward == -10:
            penalties += 1
        if reward == -1:
            penalties += 0.1

        state = next_state
        epochs += 1

    all_epochs.append(epochs)
    all_penalties.append(penalties)
    all_rewards.append(reward)

    if i % 100 == 0:
        clear_output(wait=True)
        print(f'Episode: {i}')

print("Training finished \n")

np.savetxt('q_table2',q_table, delimiter=",")

plt.plot(all_epochs, all_penalties, label='penalties')
plt.plot(all_epochs, all_rewards, label='rewards')

plt.show()