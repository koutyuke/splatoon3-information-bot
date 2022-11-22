import discord


def createScheduleMessage(
    battleType: str, battleTypeEn: str, data: object, colorNum: tuple
):
    title = f"{battleType}\n{data['rule']}\nTime:[{data['type']}]({data['time']})"
    description = f"{data['stage'][0]}\n{data['stage'][1]}"
    color = discord.Color.from_rgb(colorNum[0], colorNum[1], colorNum[2])
    file = discord.File(
        fp=f"module/image/schedule/{battleTypeEn}/{data['type']}.jpg",
        filename=f"{battleTypeEn}{data['type']}.jpg",
        spoiler=False,
    )
    embed = discord.Embed(title=title, color=color, description=description)
    embed.set_image(url=f"attachment://{battleTypeEn}{data['type']}.jpg")
    return [embed, file]
