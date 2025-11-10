import discord
from discord.ext import commands
from utils import admin_only, update_bot, restart_bot

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name="update", description="Pull latest code and restart bot")
    @admin_only()
    async def update(self, ctx):
        if await update_bot(ctx):
            await restart_bot(self.bot)
    
    @discord.slash_command(name="restart", description="Restart the bot")
    @admin_only()
    async def restart(self, ctx):
        await ctx.respond("Restarting bot...")
        await restart_bot(self.bot)

def setup(bot):
    bot.add_cog(Admin(bot))