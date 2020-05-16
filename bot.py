import discord
import random
# import os
import subprocess
client = discord.Client();
TOKEN = open("token.key","r").readline().strip();

prefix = "comic "
# commands = ["pong","ch","random","buni","xkcd","loven","commands","help <command>"]
# commands.sort()

def loadjson(filename):
    d = {}
    with open(filename,'r') as f:
        for line in f:
            (command,info) = line.strip().split(',')
            d[command] = info
    return d

help = loadjson("help.json");
commands = list(help.keys());
commands.sort();

@client.event
async def on_ready():
    print("The bot is ready!")
    # await client.change_presence(activity=discord.Game(name="Grand Theft Auto"))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="people laugh"))
    # await client.change_presence(game=discord.Game(name="Making a bot"))

@client.event
async def on_message(message):
    if(message.author==client.user):
        return
    if(message.content.startswith(prefix)):
        command = message.content[len(prefix):]
        print(command)
        print(message.author)
        if(command == "ping"):
            await message.channel.send("pong");
        elif(command=="random"):
            await message.channel.send("Please wait sending a funny picture.")
            subprocess.call("./getrandom.sh",shell=True)
            await message.channel.send(file=discord.File('random.png'))
        elif(command=="ch"):
            await message.channel.send("Please wait sending a funny picture.")
            subprocess.call("./getch.sh",shell=True)
            await message.channel.send(file=discord.File('ch.png'))
        elif(command=="xkcd"):
            await message.channel.send("Please wait sending a funny picture.")
            subprocess.call("./getxkcd.sh",shell=True)
            await message.channel.send(file=discord.File('xkcd.png'))
        elif(command=="loven"):
            await message.channel.send("Please wait sending a funny picture.")
            subprocess.call('./getloven.sh',shell=True)
            await message.channel.send(file=discord.File('loven.png'))
        elif(command=="buni"):
            await message.channel.send("Please wait sending a funny picture.")
            subprocess.call('./getbuni.sh',shell=True)
            await message.channel.send(file=discord.File('buni.png'))
        elif(command=="garfield"):
            await message.channel.send("Please wait sending a funny picture.")
            subprocess.call('./getgarfield.sh',shell=True)
            await message.channel.send(file=discord.File('garfield.png'))
        elif(command[:4]=="kill"):
            # await message.channel.send("@%s who do you want to kill?"%message.author)
            person1 = message.author.mention
            id = command[5:]
            if(len(id)<1):
                personb = client.user.mention
                await message.channel.send(f"{personb} killed {person1} for incomplete command.")
            else:
                await message.channel.send(f"Sutron se pata chala hai ki %s ki hatya {person1} ke haathon hone wali h" % id)
        # elif(command=="changeprefix"):
        elif(command=="commands"):
            reply = "The list of valid commands is "
            for c in commands :
                reply += ("`" + c + "` ") + ","
            # reply = reply[]
            await message.channel.send(reply[:-1])
        elif(command[:4]=="help"):
            if(len(command)>4):
                command = command[5:]
                if(command in help):
                    await message.channel.send("`"+command+"`: "+help[command]);
                else:
                    await message.channel.send("Not a valid command");
            else:
                await message.channel.send("Please select a command for seeking help about.")
        else:
            await message.channel.send("Fucking retard! Enter a valid command next time!");

client.run(TOKEN);
