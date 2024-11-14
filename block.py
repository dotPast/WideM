from beet import Context, Texture
from PIL import Image


def gravel(ctx: Context):
    ctx.assets["minecraft:block/gravel"] = Texture(
        Image.open("./assets/textures/block/gravel.png")
    )

    ctx.assets["minecraft:block/suspicious_gravel_0"] = Texture(
        Image.open("./assets/textures/block/suspicious_gravel.png")
    )

    ctx.assets["minecraft:block/suspicious_gravel_1"] = Texture(
        Image.open("./assets/textures/block/suspicious_gravel.png")
    )

    ctx.assets["minecraft:block/suspicious_gravel_2"] = Texture(
        Image.open("./assets/textures/block/suspicious_gravel.png")
    )

    ctx.assets["minecraft:block/suspicious_gravel_3"] = Texture(
        Image.open("./assets/textures/block/suspicious_gravel.png")
    )


def furnace(ctx: Context):
    ctx.assets["minecraft:block/furnace_front"] = Texture(
        Image.open("./assets/textures/block/furnace/front.png")
    )

    ctx.assets["minecraft:block/furnace_front_on"] = Texture(
        Image.open("./assets/textures/block/furnace/front_on.png")
    )

    ctx.assets["minecraft:block/furnace_side"] = Texture(
        Image.open("./assets/textures/block/furnace/side.png")
    )

    ctx.assets["minecraft:block/furnace_top"] = Texture(
        Image.open("./assets/textures/block/furnace/side.png")
    )
