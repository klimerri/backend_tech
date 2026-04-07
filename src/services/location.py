def validate_location(location):
    if location.house <= 0:
        raise ValueError("House number must be positive")
    return location