import math


def calculate_direction(start_point, end_point):
    delta_lat = math.radians(end_point[0] - start_point[0])
    delta_lon = math.radians(end_point[1] - start_point[1])
    direction = math.degrees(math.atan2(delta_lon, delta_lat))
    if direction < 0:
        direction = direction + 360
    return direction


def calculate_distance(start_point, end_point):
    radius = 6371.0
    lat1 = math.radians(start_point[0])
    lon1 = math.radians(start_point[1])
    lat2 = math.radians(end_point[0])
    lon2 = math.radians(end_point[1])
    difference_lat = lat2 - lat1
    difference_lon = lon2 - lon1
    a = math.sin(difference_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(difference_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c
    return distance


def conversion_km_to_nm(dist):
    conv_fact = 1.852  # conversion factor km to nautical mile
    distance = dist / conv_fact
    return distance
