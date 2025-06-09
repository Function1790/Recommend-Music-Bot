# str.split 메서드 변형(''인 아이템은 반환 X)
def split(str, keyword):
  '''Remove null item'''
  return [i for i in str.split(keyword) if i!='']

# music.txt 파일 불러오기
def loadMusicFile():
  f = open("music.txt", "r", encoding="utf8")
  data = f.read()
  f.close()
  return data

# music.txt 파일 파싱
def parseMusicData(filedata:str):
  '''
  return parsed[janre][music]
  [janre][0]  => janre description
  [janre][1:] => recommended music
  '''
  parsed = split(filedata, "#")
  parsed = [split(i, "\n") for i in parsed]
  return parsed