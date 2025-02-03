from .conf import conf
from .shapes.circle import Circle


class Ship:
    """Ship."""

    def __init__(self, y):
        """Construct."""
        self.y = y
        self.y_values = []

    def build(self):
        """Draw."""
        tail = []
        tail.append(
            Circle(
                size=conf["ship"]["size"],
                opacity=1.0,
                centre=(conf["ship"]["x-offset"], self.y),
            )
        )

        for index, value in enumerate(reversed(self.y_values)):
            tail.append(
                Circle(
                    size=conf["ship"]["size"]
                    * (
                        (conf["ship"]["tail"]["length"] - (index + 1))
                        / conf["ship"]["tail"]["length"]
                    ),
                    centre=(
                        conf["ship"]["x-offset"]
                        - (index * conf["ship"]["tail"]["spacing"])
                        - conf["ship"]["tail"]["spacing"],
                        value,
                    ),
                    opacity=(conf["ship"]["tail"]["length"] - index)
                    / conf["ship"]["tail"]["length"],
                )
            )

        self.y_values.append(self.y)
        if len(self.y_values) > conf["ship"]["tail"]["length"]:
            self.y_values = self.y_values[1:]

        return tail
