import random
import numpy as np
import decimal

class epsilon_greedy:

    def __init__(self, actions, rewards):
        self.values = [0 for i in range(len(actions))]
        self.actions = actions
        self.rewards = rewards
        self.n = [0 for i in range(len(actions))]
        self.e = 0.5
        self.k = len(actions)
    
    def pick(self):
        e = self.epsilon()
        print(e)
        if e > self.e:
            result = self.exploit()
        else:
            result = self.explore()
        return result

    def shrink_e(self):
        self.e = self.e-0.01

    def epsilon(self):
        return float(decimal.Decimal(random.randrange(0, 100))/100)

    def update_value(self,i):
        self.n[i] = self.n[i] + 1
        self.values[i] = self.values[i] + (1/self.n[i])*(self.rewards[i] - self.values[i])

    def exploit(self):
        max_value_index = np.argmax(self.values)
        self.update_value(max_value_index)
        print("exploitation move")
        return self.actions[max_value_index]

    def explore(self):
        item_i = random.randint(0, self.k-1)
        self.update_value(item_i)
        #self.shrink_e()
        print("exploration move")
        return self.actions[item_i]


def k_armed(bandits ,rewards):
    actions = []
    for i in range(1, len(rewards)+1):
        actions.append('a'+str(i))
    eg = epsilon_greedy(actions, rewards)
    for i in  range(100):
        picked = eg.pick()
        print(f"iteration {i} bandit picked is --{picked}--, {bandits[actions.index(picked)]}")
        print(eg.values)

bandits = ["item"+str(i) for i in range(1, 11)]

rewards = [1, -1, 2, 5, 4, 1, 8, 2, 1, 7]

k_armed(bandits, rewards)
