from env import GridEnvironment
from agent import Robot
from vis import GridVisualizer

env = GridEnvironment(10, 50, 50)
env.input_manually()

robot = Robot(environment=env, alpha=0.1, gamma=0.9, epsilon=0.4)
robot.train(4000)

visualizer=GridVisualizer(env,robot)
x=int(input())
y=int(input())
visualizer.setStart(x,y)
#visualizer.draw_grid()
visualizer.run_visualization()