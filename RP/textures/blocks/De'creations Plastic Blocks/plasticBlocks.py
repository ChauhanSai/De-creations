from PIL import Image

def colorAvg(a,b):
  ar, ag, ab = a
  br, bg, bb = b
  r = round((ar+br)/2)
  g = round((ag+bg)/2)
  b = round((ab+bb)/2)
  string=str(r)
  string+=', '
  string+=str(g)
  string+=', '
  string+=str(b)
  string+=', '
  return eval(string)

colors = ['black', 'blue', 'brown', 'cyan', 'gray', 'green', 'light_blue', 'lime', 'magenta', 'orange', 'pink', 'purple', 'red', 'silver', 'white', 'yellow']

for i in range(len(colors)):
  color=colors[i]

  powdername='concrete_powder_'
  powdername+=color
  powdername+='.png'

  plasticname='plastic_'
  plasticname+=color
  plasticname+='.png'

  concreteIm = Image.open(powdername, 'r')
  concrete = concreteIm.load()

  a = concrete[0,0]
  e = concrete[0,0]

  for y in range(16):
    for x in range(16):
      pixel = concrete[x, y]
      if e < pixel:
          e = concrete[x,y]
      if a > pixel:
          a = concrete[x,y]
  c = colorAvg(a,e)
  b = colorAvg(a,c)
  d = colorAvg(c,e)

  plasticIm = Image.open(plasticname)
  plastic = plasticIm.load()

  for y in range(16):
    for x in range(16):
      plastic[x,y] = b
      
  plasticIm.save(plasticname)
