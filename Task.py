# -*- coding: utf-8 -*-
"""
@Time ： 2023-11-01 12:07
@Auth ： Huailing Ma
@File ：Task.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

class Task:
    """This class represents functions related to task
                Attributes:
                    i      The identity of the Task
                    BW     The offered bandwidth
                    c      The maximum number of drones
    """
    def __init__(self, i, BW, c):
        self.i = i
        self.BW = BW
        self.c = c