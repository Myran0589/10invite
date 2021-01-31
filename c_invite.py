import discord
from discord.ext import commands
import logging
from asyncio import sleep

logging.basicConfig(level=logging.INFO)
bot = commands.Bot(command_prefix="%")

@bot.command()
async def ten(ctx):
    channel = bot.get_channel(776025871227420692)
    await ctx.send(f"Here are 10 invites.\n")
    for count in range(1, 11):
        await sleep(0.7)
        link = await channel.create_invite(max_age=120, max_uses=1, unique=True, reason="bot command")
        await ctx.send(f" Invite {count}: {link} \n"
                       f"(valid for: {link.max_age} seconds. uses: {link.max_uses}.)")

bot.run("Token here")
