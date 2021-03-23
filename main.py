#takes parameters: lambda, number of files N, F_s params, F_p params,
#consts: access link bandwidth Ra, round trip prop time btw network and serv D, institution network bandwidth Rc
#in cache response time : S_i / R_c
#not in cache = D+ Qd + Si / Ra + Si / Rc
#outputs = avg rtt

import sys
#contains event information
class Event:
    def __init__(self, arrival_time, size, id,):
        self.arrival_time = arrival_time
        self.size = size
        self.id = id

#input validation
def check_inputs():
    arg_list=[]
    arg_remind=["Number of files", "Poisson process with rate lambda","Cache storage","Ra","Rc","D","Pareto distribution k", "Pareto distribution alpha"]
    for i in range(0, 8):
        print("please input"+" "+arg_remind[i]+":")
        arg = float(input())
        arg_list.append(arg)

    alpha_p = float(arg_list[7])
    if not (alpha_p > 1):
        print("mu_p must be greater than 1.")
        exit()
    return arg_list
    exit()




