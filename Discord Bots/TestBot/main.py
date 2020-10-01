import discord

class PyTestBot(discord.Client):
    async def on_ready(self):
        print('Connecté en temps que {0}!'.format(self.user))

client = PyTestBot()
client.run('NzYxMTk5MDc5Mjc4OTAzMzI2.X3XH4g._ta1KIhvEUzEr9zKaRpLy12T4AM')