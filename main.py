import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from calculations import *
from data_extraction import *
from navigation import *
from wave_occurence_diagram import *
from plot_results import *

# ############################################# Data Entrance #############################################
# Calculation parameters for power
V_ship = np.array([1.49999999999999, 1.5926, 1.7963, 2.0000, 2.2963, 2.4907, 2.7963, 2.9907, 3.2963, 3.4815, 3.6759,
                   3.8056, 4.0000, 4.1574, 4.2870, 4.4815, 4.6481, 4.7963, 4.9815, 5.0741, 5.1852, 5.2963, 5.3889,
                   5.4815, 5.7037, 5.8056, 5.9907])
P_E = np.array([0.091019417, 0.121359223, 0.151699029, 0.242718447, 0.333737864, 0.424757282, 0.606796117, 0.72815534,
                1.031553398, 1.243932039, 1.516990291, 1.759708738, 2.39684466, 3.185679612, 4.004854369, 5.248786408,
                6.280339806, 7.281553398, 9.01092233, 10.04247573, 11.49878641, 13.0157767, 14.53276699, 15.77669903,
                18.17354369, 19.14441748, 20.8131068])
w_T = 0.0047  # wake fraction
t = 0.0012  # thrust deduction check again
eta_R = 1  # relative rotative efficiency
eta_O = 0.55  # open water efficiency (worst case scenario)
eta_T = 0.98  # transmission losses
SCF = 1  # ship correlation factor
margins = 0.3  # sea margin

# Route Start and Arrival Coordinates
start_point = (57.6009980, -1.385616)
end_point = (57.1433128, -2.0802217)
# ############################################ Data Entrance End ############################################


# ############################################### Import data ###############################################
# Import wave data
wave_data_files = [["Point1_Hgt.csv", "Point1_Per.csv", "Point1_Dir.csv"],
                   ["Point3_Hgt.csv", "Point3_Per.csv", "Point3_Dir.csv"],
                   ["Point5_Hgt.csv", "Point5_Per.csv", "Point5_Dir.csv"]]

# Coordinates of Location 1: (57.1433128, 357.9197783) / (57.1433128, -2.0802217)
wave_height1, wave_period1, wave_direction1 = extract_wave_data(wave_data_files[0][0], wave_data_files[0][1],
                                                                wave_data_files[0][2])
# Coordinates of Location 1: (57.6009980, 358.614384) / (57.6009980, -1.385616)
wave_height3, wave_period3, wave_direction3 = extract_wave_data(wave_data_files[1][0], wave_data_files[1][1],
                                                                wave_data_files[1][2])
# Coordinates of Location 1: (57.8128588, 359.0223671) / (57.8128588, -0.9776329)
wave_height5, wave_period5, wave_direction5 = extract_wave_data(wave_data_files[2][0], wave_data_files[2][1],
                                                                wave_data_files[2][2])
# Extract availability data
availability_data = extract_data('AvData.xlsx')
# Extract Point 1 All Data
point1_data = extract_data('Route1.xlsx')

# ############################################# Import data End ##############################################

print(type(wave_height1))
print(wave_height1.shape)
print(availability_data)

# ############################################### Calculatıons ###############################################
# Calculate ship power P_S service power [kW] and P_I installed power [kW]
P_D_model, P_D_ship, P_S, P_I = calculate_power(P_E, w_T, t, eta_R, eta_O, eta_T, SCF, margins)

# Calculate heading degree and distance in km
heading = calculate_direction(start_point, end_point)
distance = calculate_distance(start_point, end_point)

# Total energy calculations
total_energy_req_S_list, total_energy_req_I_list = calculate_total_energy(distance, V_ship, P_S, P_I)

angle_differences = calculate_wave_ship_angle(heading, wave_direction1)
average_angle_differences = np.mean(angle_differences, axis=1)
max_angle_differences = np.max(angle_differences, axis=1)
# ############################################# Calculations End #############################################


# ################################################## Results ##################################################
# Plotting Power - Speed Figure
plot_figure_speed_power(V_ship, P_S, P_I)

# Plotting Total Energy - Speed Figure
plot_figure_speed_total_energy(V_ship, total_energy_req_S_list, total_energy_req_I_list)

# Print Information
plot_route_ship_info(start_point, end_point, heading, distance)
plot_power_calculations(P_E, P_D_model, P_D_ship, P_S, P_I)
plot_wave_results(wave_height1, wave_period1, wave_direction1, wave_height3, wave_period3, wave_direction3,
                  wave_height5, wave_period5, wave_direction5)

# Plot the wave directions occurrence for every month and get the occurrences data
# print_count_for_lines = True
# counts_per_months = wave_occurrence_diagram_plot(wave_direction1, print_count_for_lines)

# Print wave-vessel interaction angles differences
print(f"Angle differences:\n {angle_differences}")
print(type(angle_differences))
print(angle_differences.shape)

# Plot the figures for occurences of the wave-vessel interaction on a polar diagram divided 15 degree pieces
print_count_for_interaction = True
counts_per_directions = wave_heading_diagram_plot(angle_differences, print_count_for_interaction)

# ################################################ Results End ################################################


# ################################################ Simulation #################################################


