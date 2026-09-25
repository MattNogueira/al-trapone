import discord
from discord.ext import commands
from utils.translations import get_texts
from templates.embeds import default_embed

class CoreFunctions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_commands(self):
            return [c.name for c in self.bot.commands]
    
    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Pong! `{self.bot.latency * 1000:.0f} ms`")

    @commands.command()
    async def help(self, ctx: commands.Context):
        t = get_texts('pt-BR')
        embed = default_embed(
            title=t["help"]["title"],
            description=(t["help"]["description"]).replace("##command_prefix##", self.bot.command_prefix)
        )

        embed.add_field(name=t["help"]["commands"], value=f"`{'`, `'.join(self.get_commands())}`", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx: commands.Context):
        t = get_texts('pt-BR')
        url = "https://discord.com/oauth2/authorize?client_id=1529935908051226805"
        embed = default_embed(
            title=t["invite"]["title"],
            description=(
                f'{t["invite"]["description"]}\n\n'
                f'[{t["invite"]["link"]}]({url})'
            ),
        )

        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(CoreFunctions(bot))