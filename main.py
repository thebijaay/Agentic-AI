from agent import Agent
from environment import Environment
from utils import print_results

def main():
    # Initialize environment and agent
    env = Environment()
    agent = Agent(actions=env.get_actions())

    episodes = 5
    for episode in range(episodes):
        state = env.reset()
        done = False
        total_reward = 0

        while not done:
            action = agent.act(state)
            next_state, reward, done = env.step(action)
            agent.learn(state, action, reward, next_state)
            state = next_state
            total_reward += reward

        print_results(episode, total_reward)

if __name__ == "__main__":
    main()
  
