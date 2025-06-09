# 디스코드 봇 API 이용
import discord
from discord.ext import commands

# 제작한 모듈 불러오기
## music_loader : 음악 목록 파일을 불러오는 모듈
## env : 환경 변수 저장 파일(봇 API 토큰, 랭킹 출력 최대 순위)
## recommend : 노래 추천 알고리즘
import env, music_loader
from recommend import *

# 음악 목록 불러오기
playlist = music_loader.loadMusicFile()
playlist = music_loader.parseMusicData(playlist)

# 봇 설정
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)
userQuestionIndexes = {}

# Discord Bot command Handler
## 작동 테스트 명령 : !ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

## 질문 시작 명령 : !start
@bot.command()
async def start(ctx):
    uid = ctx.author
    print(f"start >> {uid}")
    if uid in userQuestionIndexes:
        await ctx.send("질문 인덱스를 초기화하겠습니다.")
    userQuestionIndexes[uid] = 0
    await sendQuestionByCtx(ctx, userQuestionIndexes[uid])
    userQuestionIndexes[uid] += 1

# Discord Bot event Handler
## 봇 활성화시 로그
@bot.event
async def on_ready():
    print(f'Start discord bot >> {bot.user}!')

## 봇이 메시지를 받을 때때
@bot.event
async def on_message(recv):
    if recv.author == bot.user:
        return
    
    uid = recv.author
    receiveContent = recv.content
    
    # 해당 유저가 질문 중이라면
    if uid in userQuestionIndexes:
        # 질문을 마치지 않았다면면
        if userQuestionIndexes[uid] < questionCount:
            index = userQuestionIndexes[uid]                # 현재 질문 index
            addScoreByQuestionIndex(receiveContent, index)  # 현재 질문으로 점수 더하기
            await sendQuestionByMsg(bot, recv, index)       # 디스코드로 질문 전송
            userQuestionIndexes[uid] += 1                   # index++
        else: # 질문이 끝났다면면
            soredScores = sortScores(scores)        # 점수 정렬
            content = "당신에게 추천할 음악!\n"        # 보낼 메시지
            for i in range(env.MAX_RECOMMENDATION):
                content += f"## {i+1} 순위\n" 
                index = soredScores[i][0]
                content += f'{playlist[index][0]}\n'
                for j in playlist[index][1:]:
                    content += f'- {j}\n'
            await sendOnMessage(bot, recv, content) # 추천 음악 목록 및 장르 보내기기
    
    # on_command와 on_message 중복 작동 방지
    await bot.process_commands(recv)

bot.run(env.TOKEN)