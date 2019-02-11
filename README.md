# Repository for Openmanipulator Environment





### To use

------

```
cd ~/catkin_ws/src
git clone https://github.com/kairproject/kair_manipulator_env
```

<br>

<br>

<h3>About Directory</h3>

------

`kair_manipulator_controller`, `kair_manipulator_env` 폴더는 제가 만들었습니다. 

두 폴더는 일단, ros package 단위로 만들었습니다. 

`kair_manipulator_env` 폴더는 RL script를 사용할 수 있게 하는 환경을 만드는 폴더입니다.

<br>

위 폴더들 안에 `open_manipulator_controller`패키지가 있을 것 입니다. 저희는 그 대신에 저희가 만든 제어기를 사용하므로, 제어키 코드를 넣을 폴더를 만들었습니다.

<br>

나머지 Openmanipulator, Dynamixel에 관련된 폴더는 ROBOTIS Openmanipulator 매뉴얼에 나온데로 받았습니다.

확인해보니 모든 폴더가 ros package 단위로 구성되어 있는 것은 아니고, 상위 폴더로 묶여 있는 폴더도 있습니다. 

`~/catkin_ws/src`에 그대로 넣어서 사용하시면 됩니다. 

<br>

<br>

### To Do

------

- `manipulator_env.py` 

  오픈매니퓰레이터에 `gym.GoalEnv`으로 환경을 만들 파일입니다. 

  ```python
  # It's just an example.
  
  reg = register(
      id='KairManipulator-v0',
      entry_point='kair_manipulator_env:KairManipulatorEnv',
      timestep_limit=1000,
      )
      
  class KairManipulatorEnv(gym.GoalEnv):
      # Env methods
      # ----------------------------
  	def __init__(self):
      def seed(self, seed=None):
      def step(self, action):
      def reset(self):
      def close(self):
      def render(self, mode='human'):
      # Extension methods
      # ----------------------------
  
  ```

  <br>

- `manipulator_training.py`

  q-learning 으로 샘플 코드를 만들 것입니다 .

  ```python
  # It's just an example.
  
  import manipulator_env
  
  if __name__ == '__main__':
      env = gym.make('KairManipulator-v0')
  
  ```

  <br>

- `kair_manipulator_controller`

  제어기 코드를 넣어서 활용할 수 있게 하면 될 것 같습니다. 

<br>

<br>

<h3>References</h3>

------

- http://emanual.robotis.com/docs/en/platform/openmanipulator/
- https://github.com/ROBOTIS-GIT/open_manipulator
- https://github.com/openai/gym/tree/master/gym/envs/robotics
- https://github.com/mch5048/catkin_ws_4rl/blob/master/temp_ws/src/ddpg/scripts/reaching/new_robotEnv_TD3_4D.py
- https://github.com/subinlab/rl_moving_cube
