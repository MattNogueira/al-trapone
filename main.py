import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

token = os.getenv("DISCORD_TOKEN")

print("Token encontrado?", token is not None)
print("Tem espaços nas pontas?", token != token.strip() if token else None)

if not token:
    raise RuntimeError("DISCORD_TOKEN não foi encontrada")

bot.run(token)