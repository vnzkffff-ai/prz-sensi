import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")

@bot.command()
async def sensi(ctx):
    await ctx.send("🔥 PRZ SENSI ATIVADO! 🔥\nReage aí que o pai tá on!")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency*1000)}ms")

bot.run(os.getenv("DISCORD_TOKEN"))
