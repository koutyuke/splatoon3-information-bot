import discord


def createErrorMessage(message: str):
    title = "BOT ERROR"
    color = discord.Color.from_rgb(255, 0, 0)
    description = f"message: {message}\n\nPlease contact the creator."
    embed = discord.Embed(title=title, color=color, description=description)

    return embed
