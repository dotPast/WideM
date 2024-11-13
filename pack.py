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
    ctx.assets["minecraft:gui/title/edition"] = Texture(
        Image.open("./assets/edition.png")
    )


def replace_hud(ctx: Context):
    replace_hunger(ctx)


def replace_hunger(ctx: Context):
    ctx.assets["minecraft:gui/sprites/hud/food_full"] = Texture(
        Image.open("./assets/textures/hud/hunger/full.png")
    )
    ctx.assets["minecraft:gui/sprites/hud/food_half"] = Texture(
        Image.open("./assets/textures/hud/hunger/half.png")
    )
    ctx.assets["minecraft:gui/sprites/hud/food_empty"] = Texture(
        Image.open("./assets/textures/hud/hunger/empty.png")
    )

    ctx.assets["minecraft:gui/sprites/hud/food_full_hunger"] = Texture(
        Image.open("./assets/textures/hud/hunger/full_hunger.png")
    )
    ctx.assets["minecraft:gui/sprites/hud/food_half_hunger"] = Texture(
        Image.open("./assets/textures/hud/hunger/half_hunger.png")
    )
    ctx.assets["minecraft:gui/sprites/hud/food_empty_hunger"] = Texture(
        Image.open("./assets/textures/hud/hunger/empty_hunger.png")
    )
