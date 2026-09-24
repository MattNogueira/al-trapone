from discord.ext import commands

class CoreFunctions(commands.Cog):
    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("Pong!")

async def setup(bot: commands.Bot):
    await bot.add_cog(CoreFunctions())