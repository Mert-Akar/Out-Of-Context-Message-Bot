import discord
import os
import re
from discord.ext import commands
from random import randint

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def random(ctx):
    with open("out_of_context_messages.txt", 'r', encoding = "utf-8") as message_file:
         messages = list(message_file.read().split("\n\n"))
         message_count = len(messages)
         random_index = randint(0,message_count - 1)
         await ctx.send(messages[random_index])


@bot.command()
async def add(ctx):
    if ctx.message.reference is not None:
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        with open("out_of_context_messages.txt", 'a', encoding = "utf-8") as message_file:
                message_file.write(f'\n\n{message.content}')
                await ctx.send("Message has been added to database.")
    else:
        await ctx.send("You must reply to the message you wish to add.")

TOKEN = 'insert your token here' #Don't share your token with anyone!
bot.run(TOKEN)


