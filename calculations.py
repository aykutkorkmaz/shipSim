import math
import numpy as np
from navigation import *
def calculate_power(P_E, w_T, t, eta_R, eta_O, eta_T, SCF, margins):
    eta_H = (1 - t) / (1 - w_T)
    eta_D = eta_H * eta_R * eta_O

    P_D_model = P_E / eta_D
    P_D_ship = P_D_model * SCF
    P_S = P_D_ship / eta_T
    P_I = P_S * (1 + margins)

    return P_D_model, P_D_ship, P_S, P_I

def calculate_wave_ship_angle(ship_heading, wave_direction):
    angle_difference = np.abs(ship_heading - wave_direction) % 360
    return np.where(angle_difference <= 180, angle_difference, 360 - angle_difference)

def calculate_total_energy(distance, V_ship, P_S, P_I):
    # Route 1 - Total energy calculations
    dist_nm = conversion_km_to_nm(distance)
    total_energy_req_S_list = []
    total_energy_req_I_list = []

    for i, speed in enumerate(V_ship):
        voyage_duration = dist_nm / speed

        total_energy_req_S = P_S[i] * voyage_duration
        total_energy_req_I = P_I[i] * voyage_duration

        total_energy_req_S_list.append(total_energy_req_S)
        total_energy_req_I_list.append(total_energy_req_I)

    return total_energy_req_S_list, total_energy_req_I_list
