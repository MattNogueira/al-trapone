from discord.ext import commands

class Lifecycle(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user.name} - {self.bot.user.id}")

async def setup(bot: commands.Bot):
    await bot.add_cog(Lifecycle(bot))