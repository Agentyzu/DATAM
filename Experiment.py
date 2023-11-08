# -*- coding: utf-8 -*-
"""
@Time ： 2023-11-01 11:07
@Auth ： Huailing Ma
@File ：Experiment.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

from random import *
from UAV import UAV
from Task import Task
from Bid import Bid
from ToolHelper import ToolHelper

# The sum of utility for UAVs under different δ values.
def experiment1_beta_sum_utility():
    for beta in [1, 1.2, 1.4]:
        print('beta', beta)
        for num_task in range(20, 201, 10):
            iteration = 200
            iteration_total_uav_utility = 0
            iteration_total_task_utility = 0
            num_UAV = 100
            for k in range(iteration):
                tool = ToolHelper(num_UAV, num_task)

                # Algorithm 1 is initialized
                task_arr = []

                # Initialize the task information
                total_BW = 0
                for i in range(num_task):
                    c = randint(3, 5)
                    BW = randint(20, 25)
                    total_BW += BW
                    task = Task(i, BW, c)
                    task_arr.append([task.i, task.BW, task.c])
                total_bw = total_BW / beta

                # Stores all generated UAV information
                uav_arr = []
                for i in range(num_UAV):
                    # bwj initialization
                    bw = total_bw / num_UAV
                    uav = UAV(i, bw)
                    uav_arr.append([uav.i, uav.bw])
                w1 = []

                # Generate UAV valuation information
                v_arr = []
                for i in range(num_UAV):
                    v = []
                    for j in range(num_task):
                        alpha = uniform(1, 1.5)
                        value = alpha * uav_arr[-1][-1]
                        v.append([j, value])
                    v_arr.append(v)

                # Generate UAV quote information
                b = []
                for i in range(num_task):
                    bi = []
                    for j in range(num_UAV):
                        bij = v_arr[j][i][-1]
                        bi.append([j, bij])
                    b.append(bi)
                bid = Bid(task_arr, uav_arr, b)
                w1 = bid.bid_store()
                w1 = bid.descending_sort()
                w2 = bid.seller_bid()
                p_arr = bid.seller_store()

                tool = ToolHelper(num_UAV, num_task)
                x1 = tool.win_vec(w2)

                x = [[0] * num_task for i in range(num_UAV)]

                r_arr = tool.r_arr_store()

                # An array of buyer purchase prices
                p_buy_arr, x = bid.buy_bid(x, r_arr, x1, p_arr, v_arr)

                total_uav_utility = tool.uav_total_utility(x, v_arr, uav_arr, p_buy_arr)
                total_task_utility = tool.task_total_utility(x, p_arr, uav_arr)
                iteration_total_uav_utility += total_uav_utility
                iteration_total_task_utility += total_task_utility
            avg_total_uav_utility = iteration_total_uav_utility / iteration
            avg_total_task_utility = iteration_total_task_utility / iteration
            print('num_task', num_task)
            print('avg_total_uav_utility', avg_total_uav_utility)
            print('avg_total_task_utility', avg_total_task_utility)


# The sum of utility for UAVs and tasks under different β values.
def experiment2_bandwidth_allocation_rate():
    for beta in [1, 1.2, 1.4]:
        print('beta', beta)
        bandwidth_allocation_rate_arr = []
        for num_task in range(20, 201, 10):
            iteration = 200
            num_UAV = 80
            bandwidth_allocation_rate = 0
            for k in range(iteration):
                tool = ToolHelper(num_UAV, num_task)

                # Algorithm 1 is initialized
                task_arr = []

                # Initialize the task information
                total_BW = 0
                for i in range(num_task):
                    c = randint(3, 5)
                    BW = randint(20, 25)
                    total_BW += BW
                    task = Task(i, BW, c)
                    task_arr.append([task.i, task.BW, task.c])
                total_bw = total_BW / beta

                # Stores all generated UAV information
                uav_arr = []
                for i in range(num_UAV):
                    # bwj initialization
                    bw = total_bw / num_UAV
                    uav = UAV(i, bw)
                    uav_arr.append([uav.i, uav.bw])
                w1 = []

                # Generate UAV valuation information
                v_arr = []
                for i in range(num_UAV):
                    v = []
                    for j in range(num_task):
                        alpha = uniform(1, 1.5)
                        value = alpha * uav_arr[-1][-1]
                        v.append([j, value])
                    v_arr.append(v)

                # Generate UAV quote information
                b = []
                for i in range(num_task):
                    bi = []
                    for j in range(num_UAV):
                        bij = v_arr[j][i][-1]
                        bi.append([j, bij])
                    b.append(bi)
                bid = Bid(task_arr, uav_arr, b)
                w1 = bid.bid_store()
                w1 = bid.descending_sort()
                w2 = bid.seller_bid()
                p_arr = bid.seller_store()

                tool = ToolHelper(num_UAV, num_task)
                x1 = tool.win_vec(w2)

                x = [[0] * num_task for i in range(num_UAV)]

                r_arr = tool.r_arr_store()

                # An array of buyer purchase prices
                p_buy_arr, x = bid.buy_bid(x, r_arr, x1, p_arr, v_arr)
                cnt = 0
                for i in range(num_task):
                    for j in range(num_UAV):
                        if x[j][i] == 1:
                            cnt += 1
                rate = cnt * uav_arr[-1][-1]/total_BW
                bandwidth_allocation_rate += rate
            avg_bandwidth_allocation_rate = bandwidth_allocation_rate / iteration
            bandwidth_allocation_rate_arr.append(avg_bandwidth_allocation_rate)
        print(bandwidth_allocation_rate_arr)

# The rate of bandwidth allocation under different β values.
def experiment3_alpha_sum_utility():
    for delta in [0.99, 1, 1.01, 1.02]:
        print('delta', delta)
        arr = []
        for num_task in range(3, 20, 2):
            iteration = 200
            iteration_total_uav_utility = 0
            iteration_total_task_utility = 0
            num_UAV = 10
            for k in range(iteration):
                beta = uniform(1, 1.4)
                tool = ToolHelper(num_UAV, num_task)

                # Algorithm 1 is initialized
                task_arr = []

                # Initialize the task information
                total_BW = 0
                for i in range(num_task):
                    c = randint(3, 5)
                    BW = randint(20, 25)
                    total_BW += BW
                    task = Task(i, BW, c)
                    task_arr.append([task.i, task.BW, task.c])
                total_bw = total_BW / beta
                # Stores all generated UAV information
                uav_arr = []
                for i in range(num_UAV):
                    # bwj initialization
                    bw = total_bw / num_UAV
                    uav = UAV(i, bw)
                    uav_arr.append([uav.i, uav.bw])
                w1 = []

                # Generate UAV valuation information
                v_arr = []
                for i in range(num_UAV):
                    v = []
                    for j in range(num_task):
                        alpha = uniform(1, 1.5)
                        value = alpha * uav_arr[-1][-1]
                        v.append([j, value])
                    v_arr.append(v)

                # Generate UAV quote information
                b = []
                for i in range(num_task):
                    bi = []
                    for j in range(num_UAV):
                        bij = delta * v_arr[j][i][-1]
                        bi.append([j, bij])
                    b.append(bi)
                bid = Bid(task_arr, uav_arr, b)
                w1 = bid.bid_store()
                w1 = bid.descending_sort()
                w2 = bid.seller_bid()
                p_arr = bid.seller_store()

                tool = ToolHelper(num_UAV, num_task)
                x1 = tool.win_vec(w2)

                x = [[0] * num_task for i in range(num_UAV)]

                r_arr = tool.r_arr_store()

                # An array of buyer purchase prices
                p_buy_arr, x = bid.buy_bid(x, r_arr, x1, p_arr, v_arr)
                total_uav_utility = tool.uav_total_utility(x, v_arr, uav_arr, p_buy_arr)
                total_task_utility = tool.task_total_utility(x, p_arr, uav_arr)
                iteration_total_uav_utility += total_uav_utility
                iteration_total_task_utility += total_task_utility
            avg_total_uav_utility = iteration_total_uav_utility / iteration
            avg_total_task_utility = iteration_total_task_utility / iteration
            arr.append(avg_total_uav_utility)
        print(arr)
