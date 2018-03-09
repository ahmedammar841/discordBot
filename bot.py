import random
import json
import os
import discord
import asyncio
import logging

from datetime import datetime
from math_func import factorial
from hangman import Hangman
from random import randint


logging.basicConfig(level=logging.INFO)
client = discord.Client()

# making this a global for now
game = Hangman()

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

    # print all messages to a log file
    message_log = '[' + message.timestamp.strftime('%H:%M:%S')+']' + ' ' + message.author.name + ': ' + message.content
    # make sure there aren't any illegal characters. RIP windows
    message_log = str(message_log.encode('unicode-escape'))

    # write to a log file from the script directory. create the file if it doesn't exist
    dir = os.path.dirname(__file__)
    path = 'log.txt'
    file_path = os.path.join(dir, path)
    file = open(file_path, 'a')

    # write each message on a single line
    file.write(message_log)
    file.write('\n')
    file.close()

    if message.content.startswith('!ping'):
        await client.send_message(message.channel, 'Pong')

    elif message.content.startswith('!angrave'):
        dir = os.path.dirname(__file__)
        path = 'images/angrave.jpg'
        file_path = os.path.join(dir, path)
        await client.send_file(message.channel, file_path)

    elif message.content.startswith('!choice'):
        if args[1] == 'usage':
            await client.send_message(message.channel, '```Usage: !choice [first choice, second choice, third choice...]```')
        choices = message.content.split(', ')
        choice = randint(0, len(choices)-1)
        if choice == 0 and args[1] != 'usage':
             await client.send_message(message.channel, choices[0][7:])
        elif args[1] != 'usage':
            await client.send_message(message.channel, choices[choice])

    elif message.content.startswith('!pepe'):
        await client.send_message(message.channel, ':frog::frog::frog::frog::frog::frog::frog:\n:frog::frog::frog::frog::frog::frog::frog::frog::frog:\n:frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n:frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n:frog::frog::white_circle:️:black_circle:️:black_circle:️:white_circle:️:frog::frog::frog::white_circle:️:black_circle:️:black_circle:️:white_circle:️\n:frog::white_circle:️:black_circle:️:black_circle:️:white_circle:️:black_circle:️:white_circle:️:frog::white_circle:️:black_circle:️:black_circle:️:white_circle:️:black_circle:️:white_circle:️\n:frog::white_circle:️:black_circle:️:white_circle:️:black_circle:️:black_circle:️:white_circle:️:frog::white_circle:️:black_circle:️:white_circle:️:black_circle:️:black_circle:️:white_circle:️\n:frog::frog::white_circle:️:black_circle:️:white_circle:️:white_circle:️:frog::frog::frog::white_circle:️:black_circle:️:white_circle:️:white_circle:️\n:frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n:red_circle::red_circle::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n:frog::red_circle::red_circle::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n:frog::frog::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle:\n :frog::frog::frog::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle:\n:frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n:frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n:frog::frog::frog::frog::frog::frog::frog::frog::frog:')
    
    elif message.content.startswith('!xd'):
        await client.send_message(message.channel, ':joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy:\n:joy::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::joy:\n:joy::cool::100::cool::cool::cool::100::cool::100::100::100::cool::cool::cool::joy:\n:joy::cool::100::100::cool::100::100::cool::100::cool::100::100::cool::cool::joy:\n:joy::cool::cool::100::cool::100::cool::cool::100::cool::cool::100::100::cool::joy:\n:joy::cool::cool::100::100::100::cool::cool::100::cool::cool::cool::100::cool::joy:\n:joy::cool::cool::cool::100::cool::cool::cool::100::cool::cool::cool::100::cool::joy:\n:joy::cool::cool::100::100::100::cool::cool::100::cool::cool::cool::100::cool::joy:\n:joy::cool::cool::100::cool::100::cool::cool::100::cool::cool::100::100::cool::joy:\n:joy::cool::100::100::cool::100::100::cool::100::cool::100::100::cool::cool::joy:\n:joy::cool::100::cool::cool::cool::100::cool::100::100::100::cool::cool::cool::joy:\n :joy::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::joy:\n:joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy:')
    
    elif message.content.startswith('!clean'):
        num = 0
        if args[1] == 'usage':
            await client.send_message(message.channel, '```Usage: !clean [number of messages to delete]```')
        if len(args) > 0 and args[1] != 'usage':
            num = int(args[1])
        if args[1] != 'usage':
            for i in range(num+1):
                await client.delete_message(client.messages.pop())
        client.delete_message(message)
   
    elif message.content.startswith('!factorial'):
        if args[1] == 'usage':
            await client.send_message(message.channel, '```Usage: !factorial [number to take the factorial of]```')
        else:
            if len(args) > 1:
              n = int(args[1])
              await client.send_message(message.channel, 'The factorial of ' + str(n) + ' is ' + str(factorial(n)) +'.')
    
    elif message.content.startswith('!hangman'):
        game_message = ""
        if len(args) > 1:
            if args[1] == 'start':
                game.start_game()
                game_message = 'A word has been randomly selected (all lowercase). \nGuess leters by using `!hangman x` (x is the guessed letter). \n'
            else:
                game.guess(message.content)
        await client.send_message(message.channel, game_message + game.get_game_status())

@client.event
async def on_message_delete(message):
    await client.send_message((discord.Object(id='253376951543136257')), message.author.name + '\'s message \"' + message.content + '\" was deleted')
@client.event
async def on_message_edit(before, after):
    if message.author != client.user:
        await client.send_message((discord.Object(id='253376951543136257')), before.author.name + '\'s message \"' + before.content + '\" was edited to: \"' + after.content + '\".' )

client.run('NDE5NjQ0MzU1MzQzODEwNTYz.DXzHxg.vH4XkfaakW58J1p87FfjTyGyACU')
