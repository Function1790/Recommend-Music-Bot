import numpy as np

def rev(binaryArray):
    return [[1,0][i] for i in binaryArray]

jenres = ['클래식(Classical)', '재즈(Jazz)', '팝(Pop)', '록(Rock)', '힙합(Hip-hop)', 'R&B/소울(Soul)', '컨트리(Country)', '레게(Reggae)', '디스코(Disco)', '일렉트로닉(전자음악, Electronic)', '트로트(Trot)', '발라드(Ballad)', '메탈(Metal)', '랩(Rap)']
scores = np.zeros(len(jenres))
questions = {
    # 점수는 첫번째 선택 기준
    "전통적인 음악(트로트, 포크 등) vs 현대적인 음악(팝, 힙합 등)" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

for i in questions:
    select = input(i)
    selectedScores = questions[i]
    if select != '0':
        selectedScore = rev(selectedScore)
    scores  += selectedScore