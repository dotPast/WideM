import os

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


def explosion(ctx: Context):
    for sprite in os.listdir("./assets/textures/misc/explosion/"):
        ctx.assets[f"minecraft:particle/explosion_{sprite.split(".")[0]}"] = Texture(
            Image.open(f"./assets/textures/misc/explosion/{sprite}")
        )
