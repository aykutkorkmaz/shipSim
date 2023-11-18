import pandas as pd
import numpy as np


def extract_wave_data(height, period, direction):
    wave_height = pd.read_csv(height)
    wave_period = pd.read_csv(period)
    wave_direction = pd.read_csv(direction)
    wave_height = np.array(wave_height)
    wave_period = np.array(wave_period)
    wave_direction = np.array(wave_direction)
    return wave_height, wave_period, wave_direction

def extract_data(file_path):
    table = pd.read_excel(file_path)
    return table