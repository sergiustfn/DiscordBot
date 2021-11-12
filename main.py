import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".")



@bot.command()
async def hello(ctx):
    await ctx.reply("Hello!")


@bot.command()
async def add(ctx, num1:int, num2:int):
    await ctx.reply(num1+num2)



bot.run('OTA0OTk1NDMyNzY0MTcwMjYw.YYDorQ.ghv-iGGurHMiDnKf6JBoss_1zUI')

