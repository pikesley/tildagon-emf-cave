from lib.proximity_sensors import proximity_to_bottom, proximity_to_top


def test_proximity_to_bottom():
    """Test `proximity_to_bottom`."""
    assert proximity_to_bottom(10, 10, 0) == 0
    assert proximity_to_bottom(10, 5, 0) == 5
    assert proximity_to_bottom(20, 10, 5) == 5

    assert proximity_to_bottom(20, 18, 5) == -3

    assert proximity_to_bottom(-10, -20, 5) == 5


def test_proximity_to_top():
    """Test `proximity_to_top`."""
    assert proximity_to_top(-10, -10, 0) == 0
    assert proximity_to_top(-10, -5, 0) == 5
    assert proximity_to_top(-20, -10, 5) == 5

    assert proximity_to_top(-20, -18, 5) == -3

    assert proximity_to_top(10, 20, 5) == 5

    assert proximity_to_top(56, -40, 5) == -101
