from env import GridEnvironment
from agent import Robot
from vis import GridVisualizer

env = GridEnvironment(20, 50, 50)
#env.input_manually()

robot = Robot(environment=env, alpha=0.1, gamma=0.9, epsilon=0.75)
robot.train(4000)

visualizer=GridVisualizer(env,robot)
#visualizer.draw_grid()
visualizer.run_visualization()

#print(robot.q_table[0])

#for _ in range(2):
    #visualizer = GridVisualizer(env, robot)
    #visualizer.run_visualization()