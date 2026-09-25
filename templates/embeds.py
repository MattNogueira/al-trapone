import discord

def default_embed(
    title: str,
    description: str | None = None,
    *,
    colour: discord.Colour = discord.Colour.yellow(),
) -> discord.Embed:
    embed = discord.Embed(
        title=title,
        description=description,
        colour=colour,
    )
    embed.set_footer(text="Al Trapone")
    return embed