import discord
import os
from discord.ext import commands

class AlTrapone(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("cogs.lifecycle")
        await self.load_extension("cogs.core")

def main():
    intents = discord.Intents.default()
    intents.message_content = True

    token = os.getenv("DISCORD_TOKEN")

    if not token:
        raise RuntimeError("DISCORD_TOKEN não foi encontrada")
    
    bot = AlTrapone(command_prefix=".", intents=intents)
    bot.run(token)

if __name__ == "__main__":
    main()