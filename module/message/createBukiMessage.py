import discord
from random import choice


def createBukiMessage(bukiList: list[str]):
    choiceBuki = choice(bukiList)
    choiceBukiRename = choiceBuki.replace("##", "/")

    title = "random BUKI"
    color = discord.Color.from_rgb(255, 238, 50)
    description = f"Choice BUKI is...\n\nã{choiceBukiRename}ã"
    fileName = f"{choiceBuki}.jpg"
    file = discord.File(
        fp=f"module/image/buki/{fileName}", filename="image.jpg", spoiler=False
    )

    embed = discord.Embed(title=title, color=color, description=description)
    embed.set_image(url=f"attachment://image.jpg")
    return [embed, file]
