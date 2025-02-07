def proximity_to_bottom(segment_bottom, ship_y, ship_radius):
    """How close are we to the bottom."""
    return segment_bottom - (ship_y + ship_radius)


def proximity_to_top(segment_top, ship_y, ship_radius):
    """How close are we to the top."""
    return (ship_y - ship_radius) - segment_top
