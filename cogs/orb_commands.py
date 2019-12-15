"""
Use the following link to add the bot:
https://discordapp.com/oauth2/authorize?client_id=569758271930368010&scope=bot&permissions=64
"""

import discord
from discord.ext import commands as bot_commands
import random
import os
import csv
import re

print("Base libraries successfully loaded")

# Gets constants from files. Yay interlinking
from cogs.orb_commands import COMMANDS_VERSION, COMMAND_DATA
from cogs.orb_control import allowed_channel
from utils import repo

# Assigns bot & client
bot = bot_commands.Bot(command_prefix=repo.get_prefix, help_command=None, case_insensitive=True)
client = discord.Client()


# List of extensions
# INITIAL_EXTENSIONS = [
#     "cogs.orb_commands",
#     "cogs.orb_control",
#     "cogs.orb_pins",
#     "cogs.orb_fight",
#     # "cogs.orb_economy"
# ]

# # Imports extensions
# if __name__ == '__main__':
#     for extension in INITIAL_EXTENSIONS:
#         bot.load_extension(extension)

# Implemented something more straightforward way to load all the extensions (Paige)

files = os.listdir('cogs')
files.remove('__init__.py')
for file in files:
    if file.endswith('.py'):
        file_name = file[:-3]
        bot.load_extension(f'cogs.{file_name}')



# Ping (NOW IN orb_info.py) - Paige
# @bot.command()
# async def ping(ctx):
#     if allowed_channel(ctx):
#         print("Ping received from", ctx.author.display_name)
#         await ctx.send(random.choice(["Hello!", "Ping!", "Ping received", "Pong!"]))


# # Orb bot help text
# @bot.command()
# async def help(ctx):
#     if allowed_channel(ctx):
#         print("Help request received from", ctx.author.display_name)
#         await ctx.send("Orb bot is a bot that does things. Features include:\n   - Reactions\n   - Posting Illya\n   - Ranking\nFor a list of commands see orb.commands, or check them out online at https://aribowe.github.io/orb/commands. To check the bot status, see orb.status.\nDeveloped by xiii™#0013.")

# Status
@bot.command()
async def status(ctx):
    if allowed_channel(ctx):
        print("Status requested from", ctx.author.display_name)
        embed=discord.Embed(title="", color=repo.VERSION_DATA["ColourHex"])
        embed.set_author(name="ORB STATUS")
        embed.add_field(name="Core Version", value=repo.VERSION_DATA["Version"], inline=True)
        embed.add_field(name="Core Build", value=repo.VERSION_DATA["Build"], inline=True)
        embed.add_field(name="Commands Version", value=COMMANDS_VERSION["Version"], inline=True)
        embed.add_field(name="Online Status", value=repo.ONLINE_STATUS, inline=False)
        await ctx.send(embed=embed)

# Orb bot help text
@bot.command()
async def help(ctx):
    current_channel = ctx.message.channel
    if allowed_channel(ctx):
        print("Help request received from", ctx.author.display_name)
        await ctx.send("Orb bot is a bot that does things. Features include:\n   - Reactions\n   - "
                       "Posting Illya\n   - Ranking\nFor a list of commands see orb.commands, or check "
                       "them out online at https://aribowe.github.io/orb/commands. To check the bot status, "
                       "see orb.status.\nDeveloped by xiii™#0013.")
    else:
        await current_channel.send('I do not have permission to post in this channel ;A;')

# Lists commands
@bot.command()
async def commands(ctx, target=None):
    if allowed_channel(ctx):
        output = ""
        if target is None:
            print("Command overview requested from", ctx.author.display_name)
            output += "**Accepted commands:**\n```"
            for command in COMMAND_DATA:
                output += "orb." + command + "\n"
            output += "```\n```Call a specific command for more info, or all for a full command dump```"
        elif target.upper() == "ALL":
            print("Full commands list requested from", ctx.author.display_name)
            for command in COMMAND_DATA:
                output += "```Command: " + "orb." + command + "\n"
                output += "Function: " + COMMAND_DATA[command][0] + "\n"
                output += "Arguments: " + COMMAND_DATA[command][1] + "```"
        else:
            print("Info on " + target + " requested by " + ctx.author.display_name)

            info, args = COMMAND_DATA[target]
            output += "```Command: orb." + target + "\n"
            output += "Function: " + str(info) + "\n"
            output += "Arguments: " + str(args) + "```"
            # except:
            #     print("Command not found")
            #     output = "Error: Command not found"
        await ctx.send(output)




bot.run('NjU1NDEyOTIzNTE0MDkzNjA5.XfTv1Q.6VcKwZvnTVD3oekmIBeFqCqnUig', bot=True, reconnect=True)
