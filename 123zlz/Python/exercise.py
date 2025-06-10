import time
from collections import deque, namedtuple
import gymnasium as gym
import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.losses import MSE
from tensorflow.keras.optimizers import Adam

tf.random.set_seed(42)  # 设置随机种子，确保结果可复现
MEMORY_SIZE = 100_000  # 经验回放缓冲区大小
GAMMA = 0.995  # 折扣因子
ALPHA = 1e-3  # 学习率
NUM_STEPS_FOR_UPDATE = 4  # 每隔多少步更新一次网络

env = gym.make('LunarLander-v2', render_mode='rgb_array')
env.reset()

state_size = env.observation_space.shape
num_actions = env.action_space.n
initial_state = env.reset()
action = 0
next_state, reward, done, info, _ = env.step(action)
print('State Shape:', state_size)
print('Number of actions:', num_actions)

q_network = Sequential([
    Input(shape=state_size),
    Dense(units=64, activation='relu', name='qL1'),
    Dense(units=64, activation='relu', name='qL2'),
    Dense(units=num_actions, name='qL3')
])
target_q_network = Sequential([
    Input(shape=state_size),
    Dense(units=64, activation='relu', name='tqL1'),
    Dense(units=64, activation='relu', name='tqL2'),
    Dense(units=num_actions, name='tqL3')
])
optimizer = Adam(learning_rate=ALPHA)

experience = namedtuple("Experience", field_names=["state", "action", "reward", "next_state", "done"])
@tf.function
def agent_learn(experiences, gamma):
    with tf.GradientTape() as tape:
        loss = compute_loss(experiences, gamma, q_network, target_q_network)
    gradients = tape.gradient(loss, q_network.trainable_variables)
    optimizer.apply_gradients(zip(gradients, q_network.trainable_variables))
    # 更新目标网络
    utils.update_target_network(q_network, target_q_network)
    
    
start = time.time()
num_episodes = 2000  # 总训练轮数
max_num_timesteps = 1000  # 每轮最大时间步数
total_point_history = []
num_p_av = 100  # 计算平均得分的轮数
epsilon = 1.0  # 探索率
memory_buffer = deque(maxlen=MEMORY_SIZE)
target_q_network.set_weights(q_network.get_weights())  # 初始化目标网络权重

for i in range(num_episodes):
    state = env.reset()[0]
    total_points = 0
    for t in range(max_num_timesteps):
        state_qn = np.expand_dims(state, axis=0)
        q_values = q_network(state_qn)
        action = utils.get_action(q_values, epsilon)
        next_state, reward, done, info, _ = env.step(action)
        memory_buffer.append(experience(state, action, reward, next_state, done))
        update = utils.check_update_conditions(t, NUM_STEPS_FOR_UPDATE, memory_buffer)
        if update:
            experiences = utils.get_experiences(memory_buffer)
            agent_learn(experiences, GAMMA)
        state = next_state.copy()
        total_points += reward
        if done:
            break
    total_point_history.append(total_points)
    av_latest_points = np.mean(total_point_history[-num_p_av:])
    epsilon = utils.get_new_eps(epsilon)
    print(f"\rEpisode {i+1} | Total point average of the last {num_p_av} episodes: {av_latest_points:.2f}", end="")
    if (i+1) % num_p_av == 0:
        print(f"\rEpisode {i+1} | Total point average of the last {num_p_av} episodes: {av_latest_points:.2f}")
    if av_latest_points >= 200.0:
        print(f"\n\nEnvironment solved in {i+1} episodes!")
        q_network.save('lunar_lander_model.keras')
        break
tot_time = time.time() - start
print(f"\nTotal Runtime: {tot_time:.2f} s ({(tot_time/60):.2f} min)")
utils.plot_history(total_point_history)

