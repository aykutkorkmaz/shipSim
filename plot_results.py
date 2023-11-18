from matplotlib import pyplot as plt


def plot_wave_results(wave_height1, wave_period1, wave_direction1, wave_height3, wave_period3, wave_direction3,
                      wave_height5, wave_period5, wave_direction5):
    print("Wave Data:")
    print("Location 1:")
    print(f"Wave Height:\n {wave_height1}")
    print(f"Wave Period:\n {wave_period1}")
    print(f"Wave Direction:\n {wave_direction1}")
    print("Location 3:")
    print(f"Wave Height:\n {wave_height3}")
    print(f"Wave Period:\n {wave_period3}")
    print(f"Wave Direction:\n {wave_direction3}")
    print("Location 5:")
    print(f"Wave Height:\n {wave_height5}")
    print(f"Wave Period:\n {wave_period5}")
    print(f"Wave Direction:\n {wave_direction5}")
    return


def plot_power_calculations(P_E, P_D_model, P_D_ship, P_S, P_I):
    print("\nPower Calculations:")
    print("P_E:", [f"{value:.2f}" for value in P_E])
    print("P_D_model:", [f"{value:.2f}" for value in P_D_model])
    print("P_D_ship:", [f"{value:.2f}" for value in P_D_ship])
    print("P_S:", [f"{value:.2f}" for value in P_S])
    print("P_I:", [f"{value:.2f}" for value in P_I])
    return


def plot_route_ship_info(start_point, end_point, heading, distance):
    print("\nShip Route:")
    print(f"Starting Point: {start_point}")
    print(f"Ending Point: {end_point}")
    print(f"The ship should move at a heading of {heading} degrees.")
    print(f"The distance between the points is {distance} kilometers.")
    return

def plot_figure_speed_power(V_ship, P_S, P_I):
    # Plot Speed - Power curve
    plt.figure()
    plt.plot(V_ship, P_S, marker='o', linestyle='-', color='b', label='Service Power')
    plt.plot(V_ship, P_I, marker='o', linestyle='-', color='r', label='Installed Power')

    # Add labels and title
    plt.xlabel('Ship Speed (knot)')
    plt.ylabel('Power (kW)')
    plt.title('Speed versus Power Curve')
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()
    return

def plot_figure_speed_total_energy(V_ship, total_energy_req_S_list, total_energy_req_I_list):
    plt.figure()
    plt.plot(V_ship, total_energy_req_S_list, marker='o', linestyle='-', color='b', label='Service Power')
    plt.plot(V_ship, total_energy_req_I_list, marker='o', linestyle='-', color='r', label='Installed Power')

    # Add labels and title
    plt.xlabel('Ship Speed (knot)')
    plt.ylabel('Total Energy Requirement (kWh)')
    plt.title('Speed versus Total Energy Requirements - Route 1 (Short Distance)')
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()
    return
