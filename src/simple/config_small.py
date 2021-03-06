CONFIG = {"actions_list": ["no_change", "speed_up", "speed_up_up", "slow_down", "slow_down_down"],
          "state_features": ["position", "velocity"],
          "reward": 0,
          "rewards_dict": {"goal_with_good_velocity": 40,
                           "goal_with_bad_velocity": -40,
                           "per_step_cost": -3,
                           "over_speed_near_crosswalk": -40,
                           "red_light_penalize": -40,
                           "yellow_light_penalize": -20,
                           },
          "min_velocity": 0,
          "max_velocity": 4,
          "crosswalk_max_velocity": 2,
          "crosswalk_pos": 10,
          "min_position": 0,
          "max_position": 20,
          "init_state": [0, 3],
          "goal_state": [19, 3],
          }
