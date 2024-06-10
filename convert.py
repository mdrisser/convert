def bytes_to_human(bytes, suffix="B"):
    """
    Original Code:
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


#####
## DIRECTION CONVERSION
def angle_to_card(degrees):
    if degrees >= 0 and degrees <= 11.25:
        card = "N"
    elif degrees > 11.25 and degrees <= 33.75:
        card = "NNE"
    elif degrees > 33.75 and degrees <= 56.25:
        card = "NE"
    elif degrees > 56.25 and degrees <= 78.75:
        card = "ENE"
    elif degrees > 78.75 and degrees <= 101.25:
        card = "E"
    elif degrees > 101.25 and degrees <= 123.75:
        card = "ESE"
    elif degrees > 123.75 and degrees <= 146.25:
        card = "SE"
    elif degrees > 146.25 and degrees <= 168.75:
        card = "SSE"
    elif degrees > 168.75 and degrees <= 191.25:
        card = "S"
    elif degrees > 191.25 and degrees <= 213.75:
        card = "SSW"
    elif degrees > 213.75 and degrees <= 236.25:
        card = "SW"
    elif degrees > 236.25 and degrees <= 258.75:
        card = "WSW"
    elif degrees > 258.75 and degrees <= 281.25:
        card = "W"
    elif degrees > 281.25 and degrees <= 303.75:
        card = "WNW"
    elif degrees > 303.75 and degrees <= 326.25:
        card = "NW"
    elif degrees > 326.25 and degrees <= 348.75:
        card = "NNW"
    elif degrees > 348.75 and degrees <= 360:
        card = "N"
    else:
        card = "None"

    return card
