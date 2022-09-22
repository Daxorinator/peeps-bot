from contextvars import Context
import discord


intents = discord.Intents.default()
intents.members = True

guild_ids = [673956332742901802, 896359742744698890]

peepsBot = discord.Bot(intents=intents)

@peepsBot.event
async def on_ready(self):
    print(f'Logged in as {self.user}')

@peepsBot.event
async def on_connect(self):
    print(f'Connected to Discord as {self.user}')

@peepsBot.slash_command(guild_ids=guild_ids)
async def hello(ctx):
    await ctx.respond(f"Hello {ctx.author}")

@peepsBot.slash_command(guild_ids=guild_ids)
async def stew(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/896359742744698893/916309626218246144/stew.mp4")

peepsBot.run("MTAyMjYxNjY4NDM0NDkwOTk5NA.GCt0BY.fjsa2cfoZgp_YxDE10ENFWHpHTw30y7qUnTHsA")