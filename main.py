import asyncio
import os
import discord
import threading
from discord.ext import tasks
from dotenv import load_dotenv
from pprint import pprint as p
from datetime import datetime, timedelta, timezone

from module.image.getBukiImage import getBukiImage
from module.image.getStageImage import getStageImage
from module.image.scheduleImage import createScheduleImage
from module.token.getToken import getToken
from module.message.createBukiMessage import createBukiMessage
from module.message.createErrorMesage import createErrorMessage
from module.message.createStageMessage import createStageMessage
from module.message.createscheduleMessage import createScheduleMessage
from module.info.getSchedule import getSchedule
from module.data.data import propsData

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
load_dotenv()

# testGuild = discord.Object(os.environ["TEST_GUILD_ID"])


def reload():
    global token, bukiList, status, stageList, scheduleData

    token = getToken()
    print(token)
    if token == "Invalid-AccessToken" or token == "Low-Product-Version":
        status = token
    else:
        status = "ok"
        bukiList = getBukiImage(token=token)
        stageList = getStageImage(token=token)
        scheduleData = getSchedule(token=token)
        createScheduleImage(scheduleData)


JST = timezone(timedelta(hours=+9), "JST")


@tasks.loop(seconds=60)
async def Timer():
    now = datetime.now(JST).strftime("%H:%M")
    timeArray = [
        "01:01",
        "03:01",
        "05:01",
        "07:01",
        "09:01",
        "11:01",
        "13:01",
        "15:01",
        "17:01",
        "19:01",
        "21:01",
        "23:01",
    ]
    if now in timeArray:
        reload()


@client.event
async def on_ready():
    global token, bukiList, status, stageList, scheduleData

    await client.change_presence(
        activity=discord.Game(name="Splatoon", type=discord.ActivityType.playing)
    )
    token = getToken()
    print(token)
    if token == "Invalid-AccessToken" or token == "Low-Product-Version":
        status = token
    else:
        status = "ok"
        bukiList = getBukiImage(token=token)
        stageList = getStageImage(token=token)
        scheduleData = getSchedule(token=token)
        createScheduleImage(scheduleData)

    # tree.copy_global_to(guild=testGuild)
    await tree.sync()

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


@tree.command(name="stage", description="Random 'STAGE' selection")
async def stage(ctx: discord.Interaction):
    if status == "ok":
        embed = createStageMessage(stageList=stageList)
        await ctx.response.send_message(embed=embed[0], file=embed[1])
    else:
        embed = createErrorMessage(message=status)
        await ctx.response.send_message(embed=embed)


@tree.command(name="regular", description="show regular schedule")
async def regular(ctx: discord.Interaction):
    if status == "ok":

        embeds = [
            createScheduleMessage(
                battleType="レギュラーマッチ",
                battleTypeEn="regular",
                data=data,
                colorNum=(0, 255, 0),
            )
            for data in scheduleData["regular"]
        ]

        await ctx.response.send_message(
            embeds=[embed[0] for embed in embeds], files=[embed[1] for embed in embeds]
        )
    else:
        embed = createErrorMessage(message=status)
        await ctx.response.send_message(embed=embed)


@tree.command(name="open", description="show open schedule")
async def open(ctx: discord.Interaction):
    if status == "ok":

        embeds = [
            createScheduleMessage(
                battleType="バンカラマッチ(オープン)",
                battleTypeEn="open",
                data=data,
                colorNum=(255, 165, 0),
            )
            for data in scheduleData["open"]
        ]

        await ctx.response.send_message(
            embeds=[embed[0] for embed in embeds], files=[embed[1] for embed in embeds]
        )
    else:
        embed = createErrorMessage(message=status)
        await ctx.response.send_message(embed=embed)


@tree.command(name="challenge", description="show challenge schedule")
async def challenge(ctx: discord.Interaction):
    if status == "ok":

        embeds = [
            createScheduleMessage(
                battleType="バンカラマッチ(チャレンジ)",
                battleTypeEn="challenge",
                data=data,
                colorNum=(255, 165, 0),
            )
            for data in scheduleData["challenge"]
        ]

        await ctx.response.send_message(
            embeds=[embed[0] for embed in embeds], files=[embed[1] for embed in embeds]
        )
    else:
        embed = createErrorMessage(message=status)
        await ctx.response.send_message(embed=embed)


@tree.command(name="x", description="show X schedule")
async def x(ctx: discord.Interaction):
    if status == "ok":

        embeds = [
            createScheduleMessage(
                battleType="Xマッチ",
                battleTypeEn="x",
                data=data,
                colorNum=(0, 250, 154),
            )
            for data in scheduleData["x"]
        ]

        await ctx.response.send_message(
            embeds=[embed[0] for embed in embeds], files=[embed[1] for embed in embeds]
        )
    else:
        embed = createErrorMessage(message=status)
        await ctx.response.send_message(embed=embed)


@tree.command(name="league", description="show league schedule")
async def league(ctx: discord.Interaction):
    if status == "ok":

        embeds = [
            createScheduleMessage(
                battleType="リーグマッチ",
                battleTypeEn="league",
                data=data,
                colorNum=(255, 20, 147),
            )
            for data in scheduleData["league"]
        ]

        await ctx.response.send_message(
            embeds=[embed[0] for embed in embeds], files=[embed[1] for embed in embeds]
        )
    else:
        embed = createErrorMessage(message=status)
        await ctx.response.send_message(embed=embed)


@tree.command(name="now", description="show now schedule")
async def now(ctx: discord.Interaction):
    if status == "ok":

        embeds = [
            createScheduleMessage(
                battleType=propsData[ruleType]["battleType"],
                battleTypeEn=ruleType,
                data=scheduleData[ruleType][0],
                colorNum=propsData[ruleType]["color"],
            )
            for ruleType in ["regular", "open", "challenge", "x", "league"]
        ]

        await ctx.response.send_message(
            embeds=[embed[0] for embed in embeds], files=[embed[1] for embed in embeds]
        )
    else:
        embed = createErrorMessage(message=status)
        await ctx.response.send_message(embed=embed)


@tree.command(name="next", description="show next schedule")
async def next(ctx: discord.Interaction):
    if status == "ok":

        embeds = [
            createScheduleMessage(
                battleType=propsData[ruleType]["battleType"],
                battleTypeEn=ruleType,
                data=scheduleData[ruleType][1],
                colorNum=propsData[ruleType]["color"],
            )
            for ruleType in ["regular", "open", "challenge", "x", "league"]
        ]

        await ctx.response.send_message(
            embeds=[embed[0] for embed in embeds], files=[embed[1] for embed in embeds]
        )
    else:
        embed = createErrorMessage(message=status)
        await ctx.response.send_message(embed=embed)


@tree.command(name="nextnext", description="show nextnext schedule")
async def nextnext(ctx: discord.Interaction):
    if status == "ok":

        embeds = [
            createScheduleMessage(
                battleType=propsData[ruleType]["battleType"],
                battleTypeEn=ruleType,
                data=scheduleData[ruleType][2],
                colorNum=propsData[ruleType]["color"],
            )
            for ruleType in ["regular", "open", "challenge", "x", "league"]
        ]

        await ctx.response.send_message(
            embeds=[embed[0] for embed in embeds], files=[embed[1] for embed in embeds]
        )
    else:
        embed = createErrorMessage(message=status)
        await ctx.response.send_message(embed=embed)


@client.event
async def on_command_error(error):
    print(error)


async def runTimer():
    await Timer.start()


def loop():
    loop_ = asyncio.new_event_loop()
    asyncio.set_event_loop(loop=loop_)
    loop_.run_until_complete(runTimer())


def bot():
    client.run(os.environ["DISCORD_BOT_TOKEN"])


if __name__ == "__main__":
    threadLoop = threading.Thread(target=loop)
    threadBot = threading.Thread(target=bot)

    threadLoop.start()
    threadBot.start()
    threadLoop.join()
    threadBot.join()
