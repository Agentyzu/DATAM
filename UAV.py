# -*- coding: utf-8 -*-
"""
@Time ： 2023-11-01 09:07
@Auth ： Huailing Ma
@File ：UAV.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

class UAV:
    """This class represents functions related to UAV
                    Attributes:
                        i      The identity of the Task
                        bw     The requested bandwidth
    """
    def __init__(self, i, bw):
        self.i = i
        self.bw = bw