import matplotlib.pyplot as plt
import numpy as np


def wave_occurrence_diagram_plot(wave_direction, count_for):
    # Define the number of months and month names
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]

    # Define angle ranges
    angle_ranges = np.arange(0, 361, 15)

    # Initialize dictionaries to store counts for each month
    counts_per_month = {}

    # Loop through each month
    for month_index, month_name in enumerate(months):
        # Calculate angles for the current month
        wave_ship_interaction_month = np.array(wave_direction)
        angles_month = wave_ship_interaction_month[:, month_index]

        # Initialize an array to store the counts
        counts_month = np.zeros(len(angle_ranges) - 1, dtype=int)

        # Loop through the angle ranges and count occurrences for the current month
        for i in range(len(angle_ranges) - 1):
            start_angle = angle_ranges[i]
            end_angle = angle_ranges[i + 1]
            counts_month[i] = np.sum((angles_month >= start_angle) & (angles_month < end_angle))

        # Store the counts for the current month
        counts_per_month[month_name] = counts_month

    # Print the counts for each month
    if count_for:
        for month_name in months:
            counts_month = counts_per_month[month_name]
            print(f"Counts for {month_name}:")
            for i in range(len(angle_ranges) - 1):
                print(f"Count for ({angle_ranges[i]}-{angle_ranges[i + 1]} degrees): {counts_month[i]}")

    # Initialize a color map for the heat bar
    cmap = plt.get_cmap("hot")

    # Loop through each month
    for month_index, month_name in enumerate(months):
        # Get the counts for the current month
        counts_month = counts_per_month[month_name]

        # Create a circular figure
        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111, polar=True)

        # Convert angles to radians
        angles = [angle * 2 * np.pi / 360 for angle in angle_ranges]

        # Plot the data with a heat bar
        for i in range(len(angle_ranges) - 1):
            start_angle = angle_ranges[i]
            end_angle = angle_ranges[i + 1]
            count = counts_month[i]
            color = cmap(count / max(counts_month))
            ax.fill_between([angles[i], angles[i + 1]], 0, [count, count], color=color,
                            label=f"{start_angle}-{end_angle}°")

        # Set labels for each angle
        ax.set_xticks(angles)
        ax.set_xticklabels([f'{angle}°' for angle in angle_ranges])

        # Set a title
        ax.set_title(f"Wave Occurrences for {month_name}")

        # Adjust the legend position for better visibility
        ax.legend(loc="lower right", bbox_to_anchor=(0, 1), title="Angle Range", prop={'size': 3})

        # Show the plot
        plt.tight_layout()

    plt.show()

    return counts_per_month

def wave_heading_diagram_plot(angle_differences, count_for):
    # Define the number of months and month names
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]

    # Define angle ranges
    angle_ranges = np.arange(0, 181, 15)

    # Initialize dictionaries to store counts for each month
    counts_per_month = {}

    # Loop through each month
    for month_index, month_name in enumerate(months):
        # Calculate angles for the current month
        wave_ship_interaction_month = np.array(angle_differences)
        angles_month = wave_ship_interaction_month[:, month_index]

        # Initialize an array to store the counts
        counts_month = np.zeros(len(angle_ranges) - 1, dtype=int)

        # Loop through the angle ranges and count occurrences for the current month
        for i in range(len(angle_ranges) - 1):
            start_angle = angle_ranges[i]
            end_angle = angle_ranges[i + 1]
            counts_month[i] = np.sum((angles_month >= start_angle) & (angles_month < end_angle))

        # Store the counts for the current month
        counts_per_month[month_name] = counts_month

    # Print the counts for each month
    if count_for:
        for month_name in months:
            counts_month = counts_per_month[month_name]
            print(f"Counts for {month_name}:")
            for i in range(len(angle_ranges) - 1):
                print(f"Count for ({angle_ranges[i]}-{angle_ranges[i + 1]} degrees): {counts_month[i]}")

    # Initialize a color map for the heat bar
    cmap = plt.get_cmap("viridis_r")

    # Find the maximum count across all months
    max_count_across_months = max([max(counts_per_month[month_name]) for month_name in months])

    # Loop through each month
    for month_index, month_name in enumerate(months):
        # Get the counts for the current month
        counts_month = counts_per_month[month_name]

        # Create a circular figure
        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111, polar=True)

        # Convert angles to radians
        angles = [angle * 2 * np.pi / 360 for angle in angle_ranges]

        # Plot the data with a heat bar
        for i in range(len(angle_ranges) - 1):
            start_angle = angle_ranges[i]
            end_angle = angle_ranges[i + 1]
            count = counts_month[i]
            color = cmap(count / max(counts_month))
            ax.fill_between([angles[i], angles[i + 1]], 0, [count, count], color=color,
                            alpha=0.7, label=f"{start_angle}-{end_angle}°")

        # Set labels for each angle
        ax.set_xticks(angles)
        ax.set_xticklabels([f'{angle}°' for angle in angle_ranges])

        # Set a title
        ax.set_title(f"Wave-Vessel Interaction Occurrences for {month_name}")

        # Adjust the legend position for better visibility
        ax.legend(loc="lower right", bbox_to_anchor=(0, 1), title="Angle Range", prop={'size': 3})

        # Set equal limits for x and y axes
        ax.set_xlim(0, 2 * np.pi)  # Full circle
        ax.set_ylim(0, 250)  # Adjust as needed based on your data

        # Show the plot
        plt.tight_layout()

    plt.show()

    return counts_per_month
