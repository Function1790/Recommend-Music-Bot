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

for i in questions:
    select = input(i)
    selectedScoreArray = questions[i]
    if select != '0':
        selectedScoreArray = rev(selectedScoreArray)
    scores += selectedScoreArray
    
print(scores)