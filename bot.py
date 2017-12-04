import random
import json
import os
import discord
import asyncio
import logging

from math_func import factorial

logging.basicConfig(level=logging.INFO)
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    args = message.content.split(' ')

    # the bot shouldn't respond to it's own messages
    if message.author == client.user:
        return

    # print all messages to log channel
    message_log = str(message.author) + ' ' + message.content
    await client.send_message((discord.Object(id='386360744503017493')), message_log)

    if message.content.startswith('!ping'):
        await client.send_message(message.channel, 'Pong')
    elif message.content.startswith('!isevancute'):
        await client.send_message(message.channel, 'Yes, of course!')
    elif message.content.startswith('!pepe'):
        await client.send_message(message.channel, ':frog::frog::frog::frog::frog::frog::frog:\n:frog::frog::frog::frog::frog::frog::frog::frog::frog:\n:frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n:frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n:frog::frog::white_circle:️:black_circle:️:black_circle:️:white_circle:️:frog::frog::frog::white_circle:️:black_circle:️:black_circle:️:white_circle:️\n:frog::white_circle:️:black_circle:️:black_circle:️:white_circle:️:black_circle:️:white_circle:️:frog::white_circle:️:black_circle:️:black_circle:️:white_circle:️:black_circle:️:white_circle:️\n:frog::white_circle:️:black_circle:️:white_circle:️:black_circle:️:black_circle:️:white_circle:️:frog::white_circle:️:black_circle:️:white_circle:️:black_circle:️:black_circle:️:white_circle:️\n:frog::frog::white_circle:️:black_circle:️:white_circle:️:white_circle:️:frog::frog::frog::white_circle:️:black_circle:️:white_circle:️:white_circle:️\n:frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n:red_circle::red_circle::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n:frog::red_circle::red_circle::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n:frog::frog::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle:\n :frog::frog::frog::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle:\n:frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n:frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n:frog::frog::frog::frog::frog::frog::frog::frog::frog:')
    elif message.content.startswith('!xd'):
        await client.send_message(message.channel, ':joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy:\n:joy::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::joy:\n:joy::cool::100::cool::cool::cool::100::cool::100::100::100::cool::cool::cool::joy:\n:joy::cool::100::100::cool::100::100::cool::100::cool::100::100::cool::cool::joy:\n:joy::cool::cool::100::cool::100::cool::cool::100::cool::cool::100::100::cool::joy:\n:joy::cool::cool::100::100::100::cool::cool::100::cool::cool::cool::100::cool::joy:\n:joy::cool::cool::cool::100::cool::cool::cool::100::cool::cool::cool::100::cool::joy:\n:joy::cool::cool::100::100::100::cool::cool::100::cool::cool::cool::100::cool::joy:\n:joy::cool::cool::100::cool::100::cool::cool::100::cool::cool::100::100::cool::joy:\n:joy::cool::100::100::cool::100::100::cool::100::cool::100::100::cool::cool::joy:\n:joy::cool::100::cool::cool::cool::100::cool::100::100::100::cool::cool::cool::joy:\n :joy::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::joy:\n:joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy:')
    elif message.content.startswith('!clean'):
        num = 0
        if len(args) > 0:
            num = int(args[1])
        for i in range(num+1):
            await client.delete_message(client.messages.pop())
        client.delete_message(message)
    elif message.content.startswith('!fact'):
        if len(args) > 1:
            n = int(args[1])
            await client.send_message(message.channel, factorial(n))

@client.event
async def on_message_delete(message):
    await client.send_message((discord.Object(id='386360744503017493')), message.author.name + '\'s message \"'+ message.content+'\" was deleted')

client.run('Mzg2Mjc0MjgzMjI1MDg4MDAx.DQOLJw.IcnlDoxqlJrCfAdyx17tMR3tg8A')