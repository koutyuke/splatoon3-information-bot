import os
import discord
from discord.ext import tasks
from dotenv import load_dotenv
from pprint import pprint

from module.image.getBukiImage import getBukiImage
from module.token.getToken import getToken
from module.message.createBukiMessage import createBukiMessage
from module.message.createErrorMesage import createErrorMessage

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
load_dotenv()

testGuild = discord.Object(788349336287182879)


@client.event
async def on_ready():
    global token, bukiList, status

    token = getToken()
    if token == "Invalid-AccessToken" or token == "Low-Product-Version":
        status = token
    else:
        status = "ok"
        bukiList = getBukiImage(token=token)

    print(token)
    tree.copy_global_to(guild=testGuild)

    await tree.sync(guild=testGuild)

    print("login!!")


@tree.command(name="hello", description="say hello")
async def hello(
    ctx: discord.Interaction,
):
    await ctx.response.send_message("hello")


@tree.command(
    name="buki",
    description="Random 'BUKI' selection",
)
async def buki(ctx: discord.Interaction):
    if status == "ok":
        embed = createBukiMessage(bukiList=bukiList)
        await ctx.response.send_message(embed=embed[0], file=embed[1])
    else:
        embed = createErrorMessage(message=status)
        await ctx.response.send_message(embed=embed)


@client.event
async def on_command_error(error):
    print(error)


if __name__ == "__main__":
    client.run(os.environ["DISCORD_BOT_TOKEN"])
