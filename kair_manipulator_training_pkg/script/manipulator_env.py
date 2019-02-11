import gym
import rospy
import time
import numpy as np
import math
import copy

from gym.utils import seeding
from gym.envs.registration import register

reg = register(
    id='KairManipulator-v0',
    entry_point='kair_manipulator_env:KairManipulatorEnv',
    timestep_limit=1000,
    )

class KairManipulatorEnv(gym.GoalEnv):

    # Env methods
    # ----------------------------

    # def seed(self, seed=None):


    # def step(self, action):


    # def reset(self):


    # def close(self):


    # def render(self, mode='human'):


    # Extension methods
    # ----------------------------
