from beet import Context, Texture
from PIL import Image


def hunger(ctx: Context):
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
