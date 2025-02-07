from random import randint

from ..pikesley.shapes.circle import Circle
from ..pikesley.shapes.pentagram import Pentagram
from ..pikesley.shapes.triangle import Triangle
from .conf import conf

red = (255, 0, 0)
orange = (255, 127, 0)

debris = [
    {
        "shape": Circle,
        "size-factor": 1,
        "opacity-factor": 1,
        "max-distance-factor": 0,
        "count": 1,
        "colour": red,
    },
    {
        "shape": Pentagram,
        "size-factor": 1,
        "opacity-factor": 0.7,
        "max-distance-factor": 10,
        "count": 8,
        "colour": red,
    },
    {
        "shape": Triangle,
        "size-factor": 0.7,
        "opacity-factor": 0.4,
        "max-distance-factor": 20,
        "count": 16,
        "colour": orange,
    },
]


class Explosion:
    """Exploding ship."""

    def __init__(self, y):
        """Construct."""
        self.y = y

    def explode(self):
        """Draw us."""
        bits = []

        for component in debris:
            bits.extend(
                [
                    component["shape"](
                        size=conf["ship"]["size"] * component["size-factor"],
                        opacity=component["opacity-factor"],
                        centre=(
                            conf["ship"]["x-position"]
                            + randint(
                                -component["max-distance-factor"],
                                component["max-distance-factor"],
                            ),
                            self.y
                            + randint(
                                -component["max-distance-factor"],
                                component["max-distance-factor"],
                            ),
                        ),
                        colour=component["colour"],
                        rotation=randint(0, 360),
                        filled=conf["ship"]["filled"],
                    )
                    for _ in range(component["count"])
                ]
            )

        return bits
