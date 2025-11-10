import subprocess
import discord
from discord.ext import commands

def admin_only():
    """Decorator to restrict commands to administrators"""
    return commands.has_permissions(administrator=True)

async def update_bot(ctx):
    """Pull latest code from git and restart the bot"""
    await ctx.respond("Updating bot...", ephemeral=True)
    
    try:
        # Git pull
        result = subprocess.run(
            ['git', 'pull'],
            capture_output=True,
            text=True,
            check=True
        )
        
        if 'Already up to date' in result.stdout:
            await ctx.send("Already on latest version.")
            return False
        
        await ctx.send(f"Updated bot.")
        await ctx.send(f"Restarting...\n```{result.stdout}```")
        return True
        
    except subprocess.CalledProcessError as e:
        await ctx.send(f"Git pull failed.\n```{e.stderr}```")
        return False
    except Exception as e:
        await ctx.send(f"Update failed: {e}")
        return False

async def restart_bot(bot):
    """Restart the bot process"""
    import sys
    import os
    await bot.close()
    os.execv(sys.executable, ['python3'] + sys.argv)