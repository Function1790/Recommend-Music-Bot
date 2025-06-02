import discord
from discord.ext import commands
import env
import recommend

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)
userQuestionIndexes = {}

@bot.event
async def on_ready():
    print(f'Start discord bot >> {bot.user}!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! ')
    
@bot.command()
async def test(ctx):
    print(ctx.author)
    await ctx.send('Debug in Command')
    
@bot.command()
async def start(ctx):
    uid = ctx.author
    print(f"start >> {uid}")
    if uid in userQuestionIndexes:
        await ctx.send("질문 인덱스를 초기화하겠습니다.")
    userQuestionIndexes[uid] = 0
    await recommend.sendQuestion(ctx, userQuestionIndexes[uid])
    
@bot.event
async def on_message(message):
    # 봇이 자기 자신 메시지에 반응하지 않도록
    if message.author == bot.user:
        return

    # 그냥 아무 텍스트나 받기
    await message.channel.send(f"너가 보낸 메시지: {message.content}")

    # commands.Bot을 쓸 때는 이걸 추가해줘야 명령어도 작동함
    await bot.process_commands(message)

bot.run(env.TOKEN)
