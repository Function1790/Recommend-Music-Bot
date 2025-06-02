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
    await recommend.sendQuestionByCtx(ctx, userQuestionIndexes[uid])
    userQuestionIndexes[uid] += 1

@bot.event
async def on_message(recv):
    # 봇이 자기 자신 메시지에 반응하지 않도록
    if recv.author == bot.user:
        return

    # await message.channel.send(f"너가 보낸 메시지: {}")
    # await bot.process_commands(message)
    
    uid = recv.author
    receiveContent = recv.content
    if uid in userQuestionIndexes:
        if userQuestionIndexes[uid] < recommend.questionCount:
            # 유저가 질문 중 일때
            index = userQuestionIndexes[uid]
            recommend.addScoreByQuestionIndex(receiveContent, index)
            await recommend.sendQuestionByMsg(bot, recv, index)
            userQuestionIndexes[uid] += 1
        else:
            print(recommend.scores)
            await recommend.sendOnMessage(bot, recv, recommend.scores)
    await bot.process_commands(recv)
bot.run(env.TOKEN)
