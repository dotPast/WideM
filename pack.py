from beet import Context, PngFile, Texture
from PIL import Image


def setup_pack(ctx: Context):
    ctx.assets.description = 'The "M" Resource Pack. But Worse.'
    ctx.assets.icon = PngFile(source_path="./assets/icon.png")


def replace_title(ctx: Context):
    ctx.assets["minecraft:gui/title/minecraft"] = Texture(
        Image.open("./assets/title.png")
    )
    ctx.assets["minecraft:gui/title/minceraft"] = Texture(
        Image.open("./assets/title.png")
    )
