import discord
from discord import Game, Server, Member, Embed, Color

import SECRETS
import STATICS
from commands import cmd_ping

client = discord.Client()



commands = {

    "ping": cmd_ping,
}
@client.event
async def on_ready():

    print("Bot is logged in successfully.Running on servers:\n")
    for s in client.servers:
        print(" - %s (%s)" % (s.name, s.id))
    await client.change_presence(game=Game(name="This is just for tutorial purposes!"))
    # await client.send_message()

@client.event
async def on_message(message):
    #print(message.content +  " - " + message.author.name)
    if message.content.startswith(STATICS.PREFIX):
        invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commands.__contains__(invoke):
            await commands.get(invoke).ex(args, message, client, invoke)
        else:
            await client.send_message(message.channel, embed=Embed(color=Color.red(), description=("The command %s is not valid!" % invoke)))



client.run(SECRETS.TOKEN)