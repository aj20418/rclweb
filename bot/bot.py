import discord
from discord.ext import commands
import asyncio
import json

bot = commands.Bot(command_prefix="!")
filepath = "./data/teams.json"


@bot.event
async def on_ready():
    print('Logged in as:')
    print(f'Name: {bot.user.name}')
    print(f'User ID: {bot.user.id}')
    print('---------------')
    print(f'Serving for RCL')
    print('---------------')
    await bot.change_presence(game=discord.Game(name='for RCL!'))
    print('Bot is online!')

with open('config.txt', 'r') as f:
    token = f.read()


def authorized(ctx):
    '''A function to check if someone can use the json changing functions.'''
    authorized = discord.utils.get(
        bot.get_guild(352865224774385664).roles,
        id=363431233373339649
    )
    if ctx.author.top_role >= authorized:
        return True
    return False


@bot.command()
async def addteam(ctx, *, name, size: int, wins=0):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.message.channel
    if not authorized(ctx):
        return
    with open(filepath, 'r+') as f:
        teams = json.load(f)
        if teams.get(name):
            return await ctx.send('Use `!editteam` for this.')
        team = teams[name]
        team['teamSize'] = size
        team['members'] = list()
        team['subs'] = list()
        for i in range(size):
            await ctx.send('Send the next member\'s name.')
            try:
                member = bot.wait_for('message', check=check, timeout=60)
            except asyncio.TimeoutError:
                return await ctx.send('Timeout.')
            await ctx.send('Is he/she a member or substitute?')
            try:
                membership = bot.wait_for('message', check=check, timeout=60)
            except asyncio.TimeoutError:
                return await ctx.send('Timeout.')
            if membership.content.lower() == 'member':
                team['members'].append(member)
            else:
                team['subs'].append(member)
        json.dump(team, f, indent=4)
    await ctx.send(f"Team {name} was successfully registered.")


if __name__ == "__main__":
    bot.run(token)
