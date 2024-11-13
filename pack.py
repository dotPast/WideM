from beet import Context, PngFile, Texture
from PIL import Image


def setup_pack(ctx: Context):
    ctx.assets.description = 'The "M" Resource Pack. But Worse.'
    ctx.assets.icon = PngFile(source_path="./assets/icon.png")


def replace_stone(ctx: Context):
    ctx.assets["minecraft:block/stone"] = Texture(
        Image.new("RGB", (16, 16), (256, 0, 0))
    )
