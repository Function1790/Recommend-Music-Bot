def split(str, keyword):
  '''Remove null item'''
  return [i for i in str.split(keyword) if i!='']

def loadMusicFile():
  f = open("music.txt", "r", encoding="utf8")
  data = f.read()
  f.close()
  return data

def parseMusicData(filedata:str):
  '''
  return parsed[janre][music]
  [janre][0]  => janre description
  [janre][1:] => recommended music
  '''
  parsed = split(filedata, "#")
  parsed = [split(i, "\n") for i in parsed]
  return parsed