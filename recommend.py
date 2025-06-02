import numpy as np

def rev(binaryArray):
    return [[1,0][i] for i in binaryArray]

jenres = ['클래식(Classical)', '재즈(Jazz)', '팝(Pop)', '록(Rock)', '힙합(Hip-hop)', 'R&B/소울(Soul)', '컨트리(Country)', '레게(Reggae)', '디스코(Disco)', '일렉트로닉(전자음악, Electronic)', '트로트(Trot)', '발라드(Ballad)', '메탈(Metal)', '랩(Rap)']
scores = np.zeros(len(jenres))
questions = {
    # 첫번째 선택지 기준
    "전통적인 음악(트로트, 포크 등) vs 현대적인 음악(팝, 힙합 등)" : [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "혼자 부르는 음악(솔로) vs 여러 명이 부르는 음악(그룹/밴드)" : [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    "전자음(EDM, 힙합 등) vs 어쿠스틱(기타, 피아노 등)" : [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    "빠른 템포 vs 느린 템포" : [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    "시끄러운 음악 vs 잔잔한 음악" : [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    "가사가 있는 음악 vs 가사가 없는 음악" : [0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    "복잡한 멜로디 음악 vs 단순한 멜로디 음악" : [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    "즉흥적인 음악 vs 작곡된 음악" : [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "신나는 음악 vs 감성적인 음악" : [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    "밴드 음악 vs 솔로 가수 음악" : [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
}
questionsKeys = list(questions.keys())
questionCount = len(questionsKeys)

# function
def getQuestionByIndex(questionIndex:int):
    return questionsKeys[questionIndex]

def addScoreByQuestionIndex(select:str, questionIndex:int):
    global scores
    question = questionsKeys[questionIndex]
    selectedScoreArray = questions[question]
    if select != '0':
        selectedScoreArray = rev(selectedScoreArray)
    scores += selectedScoreArray

def sortDictByValue(data:dict):
    items = list(data.items())
    n = len(items)

    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] > items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items

def sortScores(scores:list):
    '''
    return items[rank][]
    [rank][0] => janre index
    [rank][1] => score
    '''
    dictScores = {i:scores[i] for i in range(len(scores))}
    return sortDictByValue(dictScores)

# bot function
async def sendQuestionByCtx(ctx, questionIndex):
    qeustion = getQuestionByIndex(questionIndex)
    await ctx.send(qeustion+" [0 또는 1을 선택하세요]")

async def sendOnMessage(bot, recv, content:str):
    await recv.channel.send(content)

async def sendQuestionByMsg(bot, msg, questionIndex:int):
    qeustion = getQuestionByIndex(questionIndex)
    await sendOnMessage(bot, msg, qeustion+" [0 또는 1을 선택하세요]")