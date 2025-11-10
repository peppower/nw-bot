import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv("../.env")

# Bot configuration
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'[SETUP] {bot.user} is now online!')
    print(f'[SETUP] Connected to {len(bot.guilds)} server(s)')
    for guild in bot.guilds:
        print(f'[SETUP] - {guild.name} (id: {guild.id})')

@bot.event
async def on_application_command_error(ctx, error):
    """Handle slash command errors"""
    print(f'[ERROR] {error}')
    await ctx.respond("Something went wrong", ephemeral=True)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'[SETUP] Loaded cog: {filename[:-3]}')

if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_TOKEN'))