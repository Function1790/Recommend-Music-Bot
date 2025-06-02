import discord
from discord.ext import commands

import env, recommend, music_loader

playlist = music_loader.loadMusicFile()
playlist = music_loader.parseMusicData(playlist)

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)
userQuestionIndexes = {}

@bot.event
async def on_ready():
    print(f'Start discord bot >> {bot.user}!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')
    
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
            soredScores = recommend.sortScores(recommend.scores)
            content = "당신에게 추천할 음악!\n"
            for i in range(env.MAX_RECOMMENDATION):
                content = f"{i+1} 순위\n"
                index = soredScores[i][0]
                content += f'{playlist[index][0]}\n'
                for j in playlist[index][1:]:
                    content += f'- {j}\n'
            await recommend.sendOnMessage(bot, recv, content)
    await bot.process_commands(recv)
bot.run(env.TOKEN)
