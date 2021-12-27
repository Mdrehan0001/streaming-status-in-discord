import discord, os, keep_alive, asyncio, datetime, pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=True
)



@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = "Rehan OP streamer", url = "https://www.twitch.tv/rehan_gamer0001"))


keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)


#this Code is made by Md Rehan enjoy and show off
