import discord
from discord.ext import commands
import env

# 봇에 사용할 명령어 접두사 (예: !ping)
bot = commands.Bot(command_prefix='!')

# 봇이 준비되었을 때 출력되는 메시지
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

# !ping 명령어에 반응
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

# 디스코드 봇 토큰 넣기 (자신의 봇 토큰으로 교체해야 함)
bot.run(env.TOKEN)
