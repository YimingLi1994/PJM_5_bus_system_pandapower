import pandapower as pp
import pandapower.networks as pn
import pandas as pd
import numpy as np
import copy
from pandapower.plotting.plotly import simple_plotly
#Network construction

net = pp.create_empty_network() #create an empty network
net.sn_kva=10000000
pp.create_bus(net, name="A", vn_kv=230, type="b", geodata=[0,0])
pp.create_bus(net, name="B", vn_kv=230, type="b", geodata=[25,0])
pp.create_bus(net, name="C", vn_kv=230, type="b", geodata=[50,0])
pp.create_bus(net, name="D", vn_kv=230, type="b", geodata=[50,50])
pp.create_bus(net, name="E", vn_kv=230, type="b", geodata=[0,50])
pp.create_ext_grid(net, bus=1, name='ext', vm_pu = 1, max_p_kw=0, min_p_kw=-0, max_q_kvar=0, min_q_kvar=-0)
pp.create_gen(net, name='Alta',      bus=0, vm_pu = 1, p_kw=-40000,  min_p_kw=-40000,   max_p_kw =0, min_q_kvar=-30000,  max_q_kvar=30000,  controllable=True)
pp.create_gen(net, name='Park City', bus=0, vm_pu = 1, p_kw=-135898, min_p_kw=-170000,  max_p_kw =0, min_q_kvar=-127500, max_q_kvar=127500, controllable=True)
pp.create_gen(net, name='Solitude',  bus=2, vm_pu = 1, p_kw=-24118, min_p_kw=-520000,  max_p_kw =0, min_q_kvar=-390000, max_q_kvar=390000, controllable=True)
pp.create_gen(net, name='Sundance',  bus=3, vm_pu = 1, p_kw=-200000, min_p_kw= -200000, max_p_kw =0, min_q_kvar=-200000, max_q_kvar=200000, controllable=True)
pp.create_gen(net, name='Brighton',  bus=4, vm_pu = 1, p_kw=-600000, min_p_kw=-600000,  max_p_kw =0, min_q_kvar=-450000, max_q_kvar=450000, controllable=True)
pp.create_polynomial_cost(net, 0, 'ext_gen', np.array([0, 10/1000, 0]))    #Brighton
pp.create_polynomial_cost(net, 0, 'gen', np.array([0, 14/1000, 0]))        #Alta
pp.create_polynomial_cost(net, 1, 'gen', np.array([0, 15/1000, 0]))        #Park City
pp.create_polynomial_cost(net, 2, 'gen', np.array([0, 30/1000, 0]))        #Solitude
pp.create_polynomial_cost(net, 3, 'gen', np.array([0, 35/1000, 0]))        #Sundancde
pp.create_polynomial_cost(net, 4, 'gen', np.array([0, 10/1000, 0]))        #Sundancde
pp.create_line_from_parameters(net, name='line1', from_bus = 0, to_bus = 1, geodata = ([0,0],[25,0]),
                               length_km= 1, r_ohm_per_km = .00281, x_ohm_per_km = 0.0281, c_nf_per_km = 0.00712, max_i_ka = 1, max_loading_percent=100)
pp.create_line_from_parameters(net, name='line2', from_bus = 0, to_bus = 3, geodata = ([0,0],[50,50]),
                               length_km= 1, r_ohm_per_km = .00304, x_ohm_per_km = 0.0304, c_nf_per_km = 0.00658, max_i_ka = 1)
pp.create_line_from_parameters(net, name='line3', from_bus = 0, to_bus = 4, geodata = ([0,0],[0,50]),
                               length_km= 1, r_ohm_per_km = .00064, x_ohm_per_km = 0.0064, c_nf_per_km = 0.03126, max_i_ka = 1)
pp.create_line_from_parameters(net, name='line4', from_bus = 1, to_bus = 2, geodata = ([25,0],[50,0]),
                               length_km= 1, r_ohm_per_km = .00108, x_ohm_per_km = 0.0108, c_nf_per_km = 0.01852, max_i_ka = 1)
pp.create_line_from_parameters(net, name='line5', from_bus = 2, to_bus = 3, geodata = ([50,0],[50,50]),
                               length_km= 1, r_ohm_per_km = .00297, x_ohm_per_km = 0.0297, c_nf_per_km = 0.00674, max_i_ka = 1)
pp.create_line_from_parameters(net, name='line6', from_bus = 3, to_bus = 4, geodata = ([50,50],[0,50]),
                               length_km= 1, r_ohm_per_km = .00297, x_ohm_per_km = 0.0297, c_nf_per_km = 0.00674, max_i_ka = 1, max_loading_percent=60)

pp.create_load(net, bus=1, p_kw=300000, q_kvar=98610)
pp.create_load(net, bus=2, p_kw=300000, q_kvar=98610)
pp.create_load(net, bus=3, p_kw=400000, q_kvar=131470)

pp.runopp(net, verbose=True)

import plotly
plotly.tools.set_credentials_file(username='chaweewatp', api_key='bWuZ24mbXFaDeinkGIGR')#API_KEY = hKAZzNC6AUqyBzEreCGZ

from pandapower.plotting.plotly import pf_res_plotly
pf_res_plotly(net)