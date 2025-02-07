from ..pikesley.rgb_from_hue.rgb_from_hue import rgb_from_hue
from .conf import conf


class Scoreboard:
    """Write the scores."""

    def __init__(self):
        """Construct."""
        self.scores = {}
        self.hue = 1.0

    def draw(self, ctx):
        """Draw ourself."""
        base_specifier = conf["scores"]["base-specifiers"][conf["scores"]["base-index"]]
        if base_specifier in ["x", "o"]:
            base_specifier = f"#{base_specifier}"

        elements = [
            {
                "text": "high score",
                "size": conf["scores"]["font-sizes"]["little"],
                "baseline": ctx.BOTTOM,
                "y": conf["scores"]["offsets"]["upper"],
            },
            {
                "text": (f"{self.scores['high-score']:{base_specifier}}"),
                "size": conf["scores"]["font-sizes"]["big"],
                "baseline": ctx.TOP,
                "y": conf["scores"]["offsets"]["upper"],
            },
            {
                "text": (f"{self.scores['score']:{base_specifier}}"),
                "size": conf["scores"]["font-sizes"]["big"],
                "baseline": ctx.BOTTOM,
                "y": conf["scores"]["offsets"]["lower"],
            },
        ]

        ctx.text_align = ctx.CENTER
        ctx.rgb(*rgb_from_hue(self.hue))

        for element in elements:
            ctx.text_baseline = element["baseline"]
            ctx.move_to(0, element["y"])
            ctx.font_size = element["size"]
            ctx.text(element["text"])
