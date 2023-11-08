# -*- coding: utf-8 -*-
"""
@Time ： 2023-11-01 13:07
@Auth ： Huailing Ma
@File ：ToolHelper.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import os
from configparser import ConfigParser

class ToolHelper:
    '''This class represents the useful tools used in the program
                Attributes:
                        num_UAV      The number of the UAVs
                        num_task     The number of the taks
                        x1           The winner determines the vector
    '''

    def __init__(self, num_UAV, num_task):
        self.num_UAV = num_UAV
        self.num_task = num_task
        self.x1 = [[0] * self.num_UAV for _ in range(self.num_task)]
        self.r_arr = []

    # This function configures initialization parameters
    def load_configuration(self):
        config_file_path = 'config.ini'
        if not os.path.exists(config_file_path):
            raise FileNotFoundError(f"Config file '{config_file_path}' does not exist")

        conn = ConfigParser()
        conn.read(config_file_path)

        # Read the configuration file and assign values to the parameters
        beta = float(conn.get('config', 'beta'))

        return beta

    # The winner determines the vector
    def win_vec(self, w2):
        p = 0
        for i in w2:
            for j in i:
                self.x1[p][j[0]] = 1
            p += 1
            if p == self.num_task:
                break
        return self.x1

    def r_arr_store(self):
        for i in range(self.num_UAV):
            r = 0
            for j in range(self.num_task):
                r += self.x1[j][i]
            self.r_arr.append(r)
        return self.r_arr

    # Calculate the total utility of UAVs
    def uav_total_utility(self, x, v_arr, uav_arr, p_buy_arr):
        total = 0
        for i in range(self.num_UAV):
            for j in range(self.num_task):
                total += x[i][j] * (v_arr[i][j][-1] - p_buy_arr[i]) * uav_arr[-1][-1]
        return total

    # Calculate the total utility of tasks
    def task_total_utility(self, x, p_arr, uav_arr):
        total = 0
        for j in range(self.num_task):
            for i in range(self.num_UAV):
                total += x[i][j] * p_arr[j] * uav_arr[-1][-1]
        return total