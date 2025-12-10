import random

class Agent:
    def __init__(self, actions):
        self.actions = actions
        self.q_table = {}  # State-action values

    def act(self, state):
        # Choose action: random for simplicity
        if state not in self.q_table:
            self.q_table[state] = {a: 0 for a in self.actions}
        return random.choice(self.actions)

    def learn(self, state, action, reward, next_state):
        # Simple learning: update Q-value
        if state not in self.q_table:
            self.q_table[state] = {a: 0 for a in self.actions}
        self.q_table[state][action] += 0.1 * (reward - self.q_table[state][action])
      
