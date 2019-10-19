# The list of valid stations
RED_LINE = ["Ashmont", "Shawmut", "Fields Corner", "Savin Hill", "JFK/UMass", "Andrew", "Broadway", "South Station",
            "Downtown Crossing", "Park St", "Charles/MGH", "Kendall", "Central", "Harvard", "Porter", "Davis",
            "Alewife"]

# List of string to uppercase
UPPERCASE_RED_LINE = []
for station in RED_LINE:
    UPPERCASE_RED_LINE.append(station.upper())
RED_LINE = UPPERCASE_RED_LINE


# # We would use list comprehension for list of string to uppercase
# RED_LINE = [element.upper() for element in RED_LINE]


def is_valid_station(station_name):
    """ Function is_valid_station
    Input: station name, a string.
    Returns: boolean, True if station is in the red line, False otherwise
    """
    station_name = station_name.upper()
    return station_name in RED_LINE
    # if station_name in RED_LINE:
    #     return True
    # else:
    #     return False


def get_direction(start_station, end_station):
    """Function get_direction
    Input: start and end stations, both strings
    Returns: first stop or last stop on the red line.
    i.  If either station doesn’t exist on the red line, return the string ​"no destination found"​.
    ii. If both stations are the same, return ​"no destination found"
    """
    start_station = start_station.upper()
    end_station = end_station.upper()
    if (start_station not in RED_LINE) or (end_station not in RED_LINE):
        return "no destination found"
    elif start_station == end_station:
        return "no destination found"
    elif RED_LINE.index(end_station) - RED_LINE.index(start_station) > 0:
        return "Alewife"
    else:
        return "Ashmont"


def get_num_stops(start_station, end_station):
    """Function get_num_stops
    Input: start and end stations, both strings
    Returns: number of stops from start to end, a positive integer.
    If either station doesn’t exist on the red line, or if both stations are the same, return 0
    """
    start_station = start_station.upper()
    end_station = end_station.upper()
    if (start_station not in RED_LINE) or (end_station not in RED_LINE):
        return 0
    elif start_station == end_station:
        return 0
    else:
        return abs(RED_LINE.index(end_station) - RED_LINE.index(start_station))
