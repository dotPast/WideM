from beet import Context, Model, Texture
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


def crafting_table(ctx: Context):
    ctx.assets.models["minecraft:block/crafting_table"] = Model(
        {
            "parent": "minecraft:block/cube",
            "textures": {
                "down": "minecraft:block/crafting_table_bottom",
                "east": "minecraft:block/crafting_table_side",
                "north": "minecraft:block/crafting_table_front",
                "particle": "minecraft:block/crafting_table_front",
                "south": "minecraft:block/crafting_table_side",
                "up": "minecraft:block/crafting_table_top",
                "west": "minecraft:block/crafting_table_front",
            },
        }
    )

    ctx.assets["minecraft:block/crafting_table_top"] = Texture(
        Image.open("./assets/textures/block/crafting_table/top.png")
    )

    ctx.assets["minecraft:block/crafting_table_front"] = Texture(
        Image.open("./assets/textures/block/crafting_table/front.png")
    )

    ctx.assets["minecraft:block/crafting_table_side"] = Texture(
        Image.open("./assets/textures/block/crafting_table/side.png")
    )

    ctx.assets["minecraft:block/crafting_table_bottom"] = Texture(
        Image.open("./assets/textures/block/crafting_table/bottom.png")
    )
