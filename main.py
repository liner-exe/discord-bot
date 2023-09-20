import nextcord
from nextcord.ext import commands
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

token = config['bot']['token']
owner_id = config['bot']['owner_id']
prefix = config['bot']['prefix']

intents = nextcord.Intents.all()

client = commands.Bot(intents=intents, command_prefix=prefix, owner_id=int(owner_id))


@client.event
async def on_ready():
    print('Logged as {0.user} (ID: {0.user.id})'.format(client),
          f'Bot is using on {len(client.guilds)} guilds!', sep='\n')


@client.event
async def on_disconnect():
    if client.is_closed():
        await client.connect()

if __name__ == '__main__':
    client.run(token)