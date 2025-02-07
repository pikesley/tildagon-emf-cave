def background_value(proximity):
    """Work out background-colour-multiplier for given proximity."""
    if proximity > 9:
        return 0

    return (10 - proximity) * 0.1
