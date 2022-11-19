import discord
from random import choice


def createStageMessage(stageList: list[str]):
    stage = choice(stageList)

    title = "random STAGE"
    color = discord.Color.from_rgb(255, 238, 50)
    description = f"Choice STAGE is...\n\n「{stage}」"
    fileName = f"{stage}.jpg"
    file = discord.File(
        fp=f"module/image/stage/{fileName}", filename="image.jpg", spoiler=False
    )

    embed = discord.Embed(title=title, color=color, description=description)
    embed.set_image(url=f"attachment://image.jpg")
    return [embed, file]
