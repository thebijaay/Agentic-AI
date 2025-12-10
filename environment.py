import random

class Environment:
    def __init__(self):
        self.states = ['state1', 'state2', 'state3']
        self.actions = ['move_left', 'move_right', 'stay']

    def reset(self):
        return random.choice(self.states)

    def step(self, action):
        # Random reward simulation
        next_state = random.choice(self.states)
        reward = random.randint(-10, 10)
        done = random.random() > 0.8  # End randomly
        return next_state, reward, done

    def get_actions(self):
        return self.actions
