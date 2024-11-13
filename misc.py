from beet import Context, Texture
from PIL import Image


def title(ctx: Context):
    ctx.assets["minecraft:gui/title/minecraft"] = Texture(
        Image.open("./assets/textures/misc/title.png")
    )
    ctx.assets["minecraft:gui/title/minceraft"] = Texture(
        Image.open("./assets/textures/misc/title.png")
    )
    ctx.assets["minecraft:gui/title/edition"] = Texture(
        Image.open("./assets/textures/misc/edition.png")
    )


def sun(ctx: Context):
    ctx.assets["minecraft:environment/sun"] = Texture(
        Image.open("./assets/textures/misc/sun.png")
    )
