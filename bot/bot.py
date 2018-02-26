import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
filepath = "../data/info.txt"
with open('config.txt', 'r') as f:
    token = f.read()
authorized = ['382574338685009920']

@bot.command()
async def write(ctx, *, body):
    if ctx.message.author.id in authorized:
        with open(filepath, 'r+') as f:
            f.write(body)
        await ctx.send(f"Wrote ```{body}``` to {filepath}.")
    else:
        await ctx.send("Not authorized.")

if __name__ == "__main__":
    bot.run(token)
