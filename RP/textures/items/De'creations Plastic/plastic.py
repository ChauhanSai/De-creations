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

  plastic[9,13] = a
  plastic[8,13] = a
  plastic[7,13] = a
  plastic[6,13] = a
  plastic[5,12] = a
  plastic[4,12] = a
  plastic[3,11] = a
  plastic[3,10] = a
  plastic[10,12] = a
  plastic[11,12] = a
  plastic[12,11] = a
  plastic[12,10] = a
  plastic[13,9] = a
  plastic[13,8] = a
  plastic[13,7] = a
  plastic[13,6] = a
  plastic[12,5] = a
  plastic[12,4] = a
  plastic[11,3] = a
  plastic[10,3] = a
  plastic[9,2] = a
  plastic[8,2] = a

  plastic[9,12] = b
  plastic[11,11] = b
  plastic[12,9] = b
  plastic[11,4] = b
  plastic[4,11] = b
  plastic[2,9] = b
  plastic[2,8] = b
  plastic[2,7] = b
  plastic[2,6] = b
  plastic[3,5] = b
  plastic[3,4] = b
  plastic[4,3] = b
  plastic[5,3] = b
  plastic[6,2] = b
  plastic[7,2] = b

  plastic[6,12] = c
  plastic[7,12] = c
  plastic[8,12] = c
  plastic[8,11] = c
  plastic[9,11] = c
  plastic[10,11] = c
  plastic[10,10] = c
  plastic[11,10] = c
  plastic[11,9] = c
  plastic[11,8] = c
  plastic[12,8] = c
  plastic[12,7] = c
  plastic[12,6] = c

  plastic[3,9] = d
  plastic[4,10] = d
  plastic[5,11] = d
  plastic[6,11] = d
  plastic[7,11] = d
  plastic[8,10] = d
  plastic[9,10] = d
  plastic[10,9] = d
  plastic[10,8] = d
  plastic[11,7] = d
  plastic[11,6] = d
  plastic[11,5] = d
  plastic[10,4] = d
  plastic[9,3] = d

  plastic[10,5] = e
  plastic[10,6] = e
  plastic[10,7] = e
  plastic[9,7] = e
  plastic[9,8] = e
  plastic[9,9] = e
  plastic[8,8] = e
  plastic[8,9] = e
  plastic[7,9] = e
  plastic[6,9] = e
  plastic[5,9] = e
  plastic[4,9] = e
  plastic[4,8] = e
  plastic[3,8] = e
  plastic[3,7] = e
  plastic[3,6] = e
  plastic[7,10] = e
  plastic[6,10] = e
  plastic[5,10] = e

  plasticIm.save(plasticname)
