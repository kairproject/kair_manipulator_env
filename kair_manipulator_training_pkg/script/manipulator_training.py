import gym
import numpy
import time
from gym import wrappers

# ROS packages required
import rospy
import rospkg

# import our training environment
# import manipulator_env

if __name__ == '__main__':
    
    # rospy.init_node('movingcube_gym', anonymous=True, log_level=rospy.WARN)

    # Create the Gym environment
    env = gym.make('KairManipulator-v0')
