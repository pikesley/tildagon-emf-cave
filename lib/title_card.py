from ..pikesley.rgb_from_hue.rgb_from_hue import rgb_from_hue
from .conf import conf


class TitleCard:
    """Title Card."""

    def __init__(self, hue):
        """Construct."""
        self.hue = hue
        self.opacity = 1.0
        self.colour = rgb_from_hue(self.hue) + [self.opacity]
        self.size = conf["title"]["size"]

    def iterate(self, hue):
        """Grow and fade."""
        self.hue = hue
        self.opacity -= conf["title"]["rates"]["fade"]
        self.colour = rgb_from_hue(self.hue) + [self.opacity]
        self.size += conf["title"]["rates"]["growth"]

    def draw(self, ctx):
        """Drow ourself."""
        ctx.move_to(0, 0)
        ctx.text_align = ctx.CENTER
        ctx.text_baseline = ctx.MIDDLE
        ctx.rgba(*self.colour)
        ctx.font_size = self.size
        ctx.text(conf["title"]["text"])
