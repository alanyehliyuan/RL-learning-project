import numpy as np
import matplotlib.pyplot as plt


class BanditEnv:
    def __init__(self, k=10, seed=42):
        self.k = k
        self.rng = np.random.default_rng(seed)
        self.true_means = self.rng.normal(loc=0.0, scale=1.0, size=k)

    def pull(self, action: int) -> float:
        return self.rng.normal(loc=self.true_means[action], scale=1.0)


class EpsilonGreedyAgent:
    def __init__(self, k=10, epsilon=0.1, seed=42):
        self.k = k
        self.epsilon = epsilon
        self.rng = np.random.default_rng(seed)
        self.q_values = np.zeros(k)
        self.action_counts = np.zeros(k, dtype=int)

    def select_action(self) -> int:
        # TODO: implement epsilon-greedy action selection
        raise NotImplementedError

    def update(self, action: int, reward: float):
        # TODO: implement incremental sample-average update
        raise NotImplementedError


def run_episode(steps=1000, epsilon=0.1):
    env = BanditEnv()
    agent = EpsilonGreedyAgent(epsilon=epsilon)
    rewards = []

    for _ in range(steps):
        action = agent.select_action()
        reward = env.pull(action)
        agent.update(action, reward)
        rewards.append(reward)

    return np.array(rewards)


def main():
    rewards = run_episode(steps=1000, epsilon=0.1)
    avg_rewards = np.cumsum(rewards) / (np.arange(len(rewards)) + 1)

    plt.plot(avg_rewards)
    plt.title('Average Reward Over Time')
    plt.xlabel('Step')
    plt.ylabel('Average Reward')
    plt.show()


if __name__ == '__main__':
    main()
