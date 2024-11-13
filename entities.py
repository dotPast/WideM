from beet import Context, Texture
from PIL import Image


def sus_creeper(ctx: Context):
    ctx.assets["minecraft:entity/creeper/creeper"] = Texture(
        Image.open("./assets/textures/entity/creeper.png")
    )
