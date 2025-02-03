from .conf import conf


class Segment:
    """A slice of a cave."""

    def __init__(self, height, centre):
        """Construct."""
        self.x = 120
        self.height = height
        self.centre = centre

    def draw(self, ctx):
        """Draw."""
        ctx.rgba(0, 0, 255, 1.0)
        ctx.move_to(self.x, self.centre - self.height / 2)
        ctx.line_to(self.x, self.centre + self.height / 2)
        ctx.line_to(
            self.x + conf["cave"]["segment-width"], self.centre + self.height / 2
        )
        ctx.line_to(
            self.x + conf["cave"]["segment-width"], self.centre - self.height / 2
        )

        ctx.fill()
