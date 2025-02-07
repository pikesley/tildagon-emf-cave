from lib.background_value import background_value


def test_background_value():
    """Test `background_value`."""
    assert background_value(20) == 0
    assert background_value(10) == 0
    assert background_value(9) == 0.1
    assert background_value(5) == 0.5
    assert round(background_value(4), 2) == 0.6
    assert background_value(1) == 0.9
    assert background_value(0) == 1.0
