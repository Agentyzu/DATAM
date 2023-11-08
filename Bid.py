# -*- coding: utf-8 -*-
"""
@Time ： 2023-11-01 10:07
@Auth ： Huailing Ma
@File ：Bid.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
class Bid:
    """This class represents functions related to bid, including the quotation and the bid

            Attributes:
                task_arr    The list of the Task
                uav_arr     The list of the UAV
                b           The list of the bid
                w1          The list of the quotation
                w2          The list of the seller's bid
                p_arr       The list of the price
        """
    def __init__(self, task_arr, uav_arr, b):
        self.task_arr = task_arr
        self.uav_arr = uav_arr
        self.b = b
        self.w1 = []
        self.w2 = [[] for _ in range(len(self.task_arr))]
        self.p_arr = []

    # Store quote information
    def bid_store(self):
        for i in self.task_arr:
            wi = []
            for j in self.uav_arr:
                if j[-1] < i[1]:
                    # Store the drone's number, as well as the UAV's quote
                    wi.append(self.b[i[0]][j[0]])
            self.w1.append(wi)
        return self.w1

    # Sort in descending order according to the quotes
    def descending_sort(self):
        for i in range(len(self.task_arr)):
            self.w1[i] = sorted(self.w1[i], key=lambda x: x[1], reverse=True)
        return self.w1

    def seller_bid(self):
        for i in range(len(self.task_arr)):
            count = 0
            sum = 0
            for j in range(len(self.w1[i])):
                if count <= self.task_arr[i][-1] and sum <= self.task_arr[i][1]:
                    self.w2[i].append(self.w1[i][j])
                    count += 1
                    sum += self.uav_arr[self.w1[i][j][0]][-1]
                else:
                    break
        return self.w2

    # Stores bid information for the task
    def seller_store(self):
        for i in range(len(self.task_arr)):
            if self.w2[i] == []:
                self.p_arr.append(0)
            else:
                self.p_arr.append(self.w2[i][-1][-1])
        return self.p_arr

    # Buyer purchase prices
    def buy_bid(self, x, r_arr, x1, p_arr, v_arr):
        p_buy_arr = [0] * len(self.uav_arr)
        final_select = [0] * len(self.uav_arr)
        for i in range(len(self.uav_arr)):
            if r_arr[i] == 0:
                x[i] = [0] * len(self.task_arr)
            elif r_arr[i] == 1:
                for j in range(len(self.task_arr)):
                    if x1[j][i] == 1:
                        final_task = j
                        final_select[i] = final_task
                        x[i][j] = 1
                        p = p_arr[j]
                        p_buy_arr[i] = p
                        break
            else:
                max = 0
                final_task = 0
                for j in range(len(self.task_arr)):
                    if x1[j][i] == 1:
                        utility = self.uav_arr[i][1] * (v_arr[i][j][-1] - p_buy_arr[i])
                        if utility > max:
                            max = utility
                            final_task = j
                            final_select[i] = final_task
                if max != 0:
                    x[i][final_task] = 1
                    p = p_arr[final_task]
                    p_buy_arr[i] = p
        return p_buy_arr, x
