from _ml import MLAgent, RandomAgent, validate, plot_validation, train, save, load, train_and_plot
from _core import is_winner, opponent, start
import random

class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
random.seed(1)
 
my_agent = load('MyAgent_3000')
random_agent = RandomAgent()
my_agent = MyAgent(alpha=0.9, epsilon=0.1)
 
train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=400,
    validations=1000)




validation_agent = RandomAgent()
 
validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
 
plot_validation(validation_result)

train(my_agent, 3000)
 
save(my_agent, 'MyAgent_3000')
start(player_x=my_agent)