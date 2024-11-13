from beet import Context, Sound, Texture
from PIL import Image


def sus_creeper(ctx: Context):
    ctx.assets["minecraft:entity/creeper/creeper"] = Texture(
        Image.open("./assets/textures/entity/creeper.png")
    )

    ctx.assets.sounds["minecraft:entity/creeper/death"] = Sound(
        open("./assets/sounds/creeper/death.ogg", "rb").read(),
        event="entity.creeper.death",
        replace=True,
    )

    ctx.assets.sounds["minecraft:entity/creeper/primed"] = Sound(
        open("./assets/sounds/creeper/primed.ogg", "rb").read(),
        event="entity.creeper.primed",
        pitch=2,
        replace=True,
    )

    ctx.assets.sounds["minecraft:entity/creeper/hurt1"] = Sound(
        open("./assets/sounds/creeper/hurt1.ogg", "rb").read(),
        event="entity.creeper.hurt",
        replace=True,
    )

    ctx.assets.sounds["minecraft:entity/creeper/hurt2"] = Sound(
        open("./assets/sounds/creeper/hurt2.ogg", "rb").read(),
        event="entity.creeper.hurt",
    )

    ctx.assets.sounds["minecraft:entity/creeper/hurt3"] = Sound(
        open("./assets/sounds/creeper/hurt3.ogg", "rb").read(),
        event="entity.creeper.hurt",
    )

    ctx.assets.sounds["minecraft:entity/creeper/hurt4"] = Sound(
        open("./assets/sounds/creeper/hurt4.ogg", "rb").read(),
        event="entity.creeper.hurt",
    )


def camel(ctx: Context):
    ctx.assets["minecraft:entity/camel/camel"] = Texture(
        Image.open("./assets/textures/entity/camel.png")
    )
