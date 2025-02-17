import numpy as np;

class Robot:
    def __init__(self, environment, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.environment = environment
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
        self.q_table = np.zeros((environment.grid_size, environment.grid_size, 4))
        self.actions = ['up', 'down', 'left', 'right']

    def choose_action(self, position):
        if np.random.uniform(0, 1) < self.epsilon:  # Explore
            return np.random.choice(self.actions)
        else:  # Exploit
            state_actions = self.q_table[position[0], position[1], :]
            return self.actions[np.argmax(state_actions)]
        
    def next_step(self, position):
        state_actions = self.q_table[position[0], position[1], :]
        return self.actions[np.argmax(state_actions)]

    def learn(self, current_position, action, reward, next_position):
        current_state_action = self.q_table[current_position[0], current_position[1], self.actions.index(action)]
        next_state_action = np.max(self.q_table[next_position[0], next_position[1], :])
        q_target = reward + self.gamma * next_state_action
        self.q_table[current_position[0], current_position[1], self.actions.index(action)] = \
            current_state_action + self.alpha * (q_target - current_state_action)

    def train(self, episodes=3000):
        for x in range(episodes):
            position = (np.random.randint(self.environment.grid_size), np.random.randint(self.environment.grid_size))
            while self.environment.grid[position] != 0:
                position = (np.random.randint(self.environment.grid_size), np.random.randint(self.environment.grid_size))

            print(f"Training episode : {x}, starting point : {position[0]}, {position[1]}")

            cnt = 0
            while position != self.environment.goal_position:
                action = self.choose_action(position)
                next_position, reward = self.environment.step(position, action)
                self.learn(position, action, reward, next_position)
                position = next_position
                cnt = cnt + 1
                if cnt == 100:
                    #print("Goal position cannot achieve by this starting point")
                    break