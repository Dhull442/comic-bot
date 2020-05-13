import discord
import random
import subprocess
client = discord.Client();
TOKEN = 'NzEwMTAwNjk5MTkwNTI2MDQy.XrvsGA.4CXIbOMHMmwGWcUm70cqYaPX9dg'
lock = 0
@client.event
async def on_ready():
    print("The bot is ready!")
    # await client.change_presence(activity=discord.Game(name="Grand Theft Auto"))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.Listening, name=" to comic "))
    # await client.change_presence(game=discord.Game(name="Making a bot"))

prefix = "comic "
commands = ["pong","pic","random","bun","xkcd","loven","commands"]
commands.sort()
# sort(commands)
@client.event
async def on_message(message):
    if(message.author==client.user):
        return
    if(message.content.startswith(prefix)):
        command = message.content[len(prefix):]
        print(command)
        if(command == "ping"):
            await message.channel.send("pong");
        elif(command=="random"):
            await message.channel.send("Please wait sending a funny picture.")
            subprocess.call("./getmeme.sh",shell=True)
            await message.channel.send(file=discord.File('img.png'))
        elif(command=="pic"):
            await message.channel.send("Please wait sending a funny picture.")
            subprocess.call("./getmade.sh",shell=True)
            await message.channel.send(file=discord.File('meme.png'))
        elif(command=="xkcd"):
            await message.channel.send("Please wait sending a funny picture.")
            subprocess.call("./getxkcd.sh",shell=True)
            await message.channel.send(file=discord.File('xkcd.png'))
        elif(command=="loven"):
            await message.channel.send("Please wait sending a funny picture.")
            subprocess.call('./getloven.sh',shell=True)
            await message.channel.send(file=discord.File('loven.png'))
        elif(command=="bun"):
            await message.channel.send("Please wait sending a funny picture.")
            subprocess.call('./getbuni.sh',shell=True)
            await message.channel.send(file=discord.File('bun.png'))
        elif(command=="commands"):
            reply = "The list of valid commands is "
            for c in commands :
                reply += ("`" + c + "` ")
            await message.channel.send(reply)
        else:
            await message.channel.send("Fucking retard! Enter a valid command next time!");

client.run(TOKEN);
