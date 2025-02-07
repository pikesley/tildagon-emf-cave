from ..pikesley.rgb_from_hue.rgb_from_hue import rgb_from_hue


class Segment:
    """A slice of a cave."""

    def __init__(self, height, width, centre, hue):
        """Construct."""
        self.x = 120
        self.height = height
        self.width = width
        self.centre = centre

        self.top = self.centre - self.height / 2
        self.bottom = self.centre + self.height / 2
        self.opacity = 1.0
        self.hue = hue
        self.colour = rgb_from_hue(self.hue) + [self.opacity]

    def draw(self, ctx):
        """Draw."""
        ctx.rgba(*self.colour)

        ctx.move_to(self.x, self.top)
        ctx.line_to(self.x, -120)
        ctx.line_to(self.x + self.width, -120)
        ctx.line_to(self.x + self.width, self.top)
        ctx.close_path()
        ctx.fill()

        ctx.move_to(self.x, self.bottom)
        ctx.line_to(self.x, 120)
        ctx.line_to(self.x + self.width, 120)
        ctx.line_to(self.x + self.width, self.bottom)
        ctx.close_path()
        ctx.fill()
